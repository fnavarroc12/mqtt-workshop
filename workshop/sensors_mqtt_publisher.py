import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
from threading import Thread
import csv
import time
import json
from sensor import generar_datos_sensor

# --- Clase MQTTPublisher ---
# Nos administrará la conexión y suscripción al broker MQTT
class MQTTPublisher:
    def __init__(self, broker_address, port, qos_level=1, username=None, password=None):
        self.broker_address = broker_address
        self.port = port
        self.qos_level = qos_level
        
        self.client = mqtt.Client(
            protocol=mqtt.MQTTv5,
            callback_api_version=CallbackAPIVersion.VERSION2
        )
        
        if username and password:
            self.client.username_pw_set(username=username, password=password)
        
        self.is_connected = False

    def connect(self):
        self.client.connect(
            host=self.broker_address, 
            port=self.port,
            keepalive=60
        )
        self.client.loop_start()
        self.is_connected = True
        print(f"Conectado al broker MQTT en {self.broker_address}:{self.port}")

    def publish(self, topic, message):
        if self.is_connected:
            result = self.client.publish(topic, message, qos=self.qos_level)
            return result
        else:
            print("No conectado al broker. Conecte primero.")
            return None

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        self.is_connected = False
        print("Desconectado del broker.")


class SensorSimulator:
    def __init__(self, base_topic: str, **broker_config):
        self.base_topic: str = base_topic
        self.publisher: MQTTPublisher = MQTTPublisher(**broker_config)
        self.measures: list = []
        self.is_runnig: bool = False
        self.thread: Thread | None = None
        
    def load_measures(self, file_path: str) -> list:
        with open(file_path, 'r') as file:
            data = list(csv.reader(file))
            
        self.measures = [(name, unit, float(vmin), float(vmax)) for name, unit, vmin, vmax in data[1:]] # Omitir la cabecera
        return self.measures
        
    def start(self, interval: int = 3):
        if not self.measures:
            raise ValueError("No hay medidas cargadas. Usa load_measures() primero.")
        
        self.publisher.connect()
        self.is_runnig = True        
        
        def run():
            msg_count = 0
            while self.is_runnig:
                for measure in self.measures:
                    topic = f"{self.base_topic}/{measure[0]}"
                    value = generar_datos_sensor(
                        measure_id=measure[0],
                        valor_min=float(measure[2]),
                        valor_max=float(measure[3])
                    )
                    message = {
                        'unit': measure[1],
                        'value': value,
                        'timestamp': time.time()
                    }
                    self.publisher.publish(topic, json.dumps(message))
                    msg_count += 1
                    print(f"\rPublicados {msg_count} mensajes", end='', flush=True)
                time.sleep(interval)
        
        self.thread = Thread(target=run)
        self.thread.start()
    
    def stop(self):
        self.is_runnig = False
        if self.thread:
            self.thread.join()
        self.publisher.disconnect()   
     
    def join(self):
        if self.thread:
            self.thread.join()
        
if __name__ == "__main__":
    simulator = SensorSimulator(
        base_topic="iot/workshop/sensor/sala1",
        broker_address="127.0.0.1",
        port=1883,
        qos_level=0,
        username="nodered",
        password="nodered"
    )
    
    simulator.load_measures("medidas_pruebas.csv")
    print(f"Cargadas {len(simulator.measures)} medidas de prueba.")
    
    try:
        print("Iniciando simulación de sensores. Presiona CTRL+C para detener.")
        simulator.start(interval=3)
        simulator.join()
            
    except KeyboardInterrupt:
        print("\nDeteniendo simulación, por favor espere...")
        simulator.stop()
        print("Simulación detenida por el usuario.")
