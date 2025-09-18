import paho.mqtt.client as mqtt
from threading import Thread
import csv
import time
import json
from sensor import generar_datos_sensor

# --- Clase MQTTPublisher ---
# Nos administrará la conexión y suscripción al broker MQTT
class MQTTPublisher:
    def __init__(self, broker_address, port, qos_level=1):
        self.broker_address = broker_address
        self.port = port
        self.qos_level = qos_level
        self.client = mqtt.Client(protocol=mqtt.MQTTv311)
        self.client.on_connect = self.on_connect
        self.client.on_publish = self.on_publish
        self.is_connected = False

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("¡Conectado exitosamente al Broker MQTT!")
            self.is_connected = True
        else:
            print(f"Fallo al conectar, código de retorno: {rc}")
            self.is_connected = False

    def on_publish(self, client, userdata, mid):
        print(f"Mensaje publicado con ID: {mid}")

    def connect(self):
        self.client.connect(self.broker_address, self.port, 60)
        self.client.loop_start()

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
        
    def load_measures(self, file_path: str) -> list:
        with open(file_path, 'r') as file:
            self.measures = list(csv.reader(file))
        return self.measures
        
    def start(self, interval: int = 3):
        if not self.measures:
            raise ValueError("No hay medidas cargadas. Usa load_measures() primero.")
        
        self.publisher.connect()
        self.is_runnig = True
        
        def run():
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
                        'value': value['value'],
                        'timestamp': value['timestamp']
                    }
                    self.publisher.publish(topic, json.dumps(message))
                time.sleep(interval)
        
        thread = Thread(target=run)
        thread.start()