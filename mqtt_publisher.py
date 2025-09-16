import paho.mqtt.client as mqtt

# --- Configuración del Cliente MQTT ---
BROKER_ADDRESS = "broker.hivemq.com"
PORT = 1883
QOS_LEVEL = 1  # 0 = At most once, 1 = At least once, 2 = Exactly once

# Usamos un comodín (+) para suscribirnos a todos los sub-topics de sensores
TOPIC = "iot/workshop/sensor/sala1/+" 

# --- Funciones de Callback ---
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("¡Conectado exitosamente al Broker MQTT!")
        # Suscribirse al topic después de una conexión exitosa
        client.subscribe(TOPIC)
    else:
        print(f"Fallo al conectar, código de retorno: {rc}")

def on_message(client, userdata, msg):
    """
    Esta función se ejecuta cada vez que se recibe un mensaje en el topic suscrito.
    """
    print(f"Mensaje recibido en el topic '{msg.topic}': {msg.payload.decode('utf-8')}")

# 1. Crear una nueva instancia de cliente, definiendo la versión del protocolo MQTT
client = mqtt.Client(protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

# 2. Conectar al broker
client.connect(BROKER_ADDRESS, PORT, 60)

# 3. Iniciar el bucle de red de forma bloqueante
# Este bucle se encarga de mantener la conexión y procesar los mensajes entrantes.
# El script se quedará aquí esperando mensajes hasta que se interrumpa.
try:
    print(f"Esperando mensajes en el topic: {TOPIC}")
    client.loop_forever()
except KeyboardInterrupt:
    print("\nSuscripción detenida.")
finally:
    client.disconnect()
    print("Desconectado del broker.")