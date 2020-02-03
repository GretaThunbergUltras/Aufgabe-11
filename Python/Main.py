import paho.mqtt.client as mqtt
from botlib.bot import Bot

MQTT_SERVER = "localhost"
MQTT_PATH = "img_capture"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_PATH)


def on_message(client, userdata, msg):
    payload = str(msg.payload)
    print(msg.topic + " " + str(payload))
    print("execMakePhoto" in payload)
    if "execMakePhoto" in payload:
        import Execute.py

try:
    print("MQTT > Starting client")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_SERVER, 1883, 60)

    client.loop_forever()
except KeyboardInterrupt:
    print("Stopping bot")
    Bot().stop_all()