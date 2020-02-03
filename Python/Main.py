import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost"
MQTT_PATH = "img_capture"

def on_connect(client, userdata, flags, rc):
    print("MQTT > Connected with result code " + str(rc))
    client.subscribe(MQTT_PATH)

def on_message(client, userdata, msg):
    payload = str(msg.payload)
    print("MQTT > topic\"{}\" payload=\"{}\"".format(msg.topic, payload))
    if "execMakePhoto" in payload:
        print("MQTT > Received start command")
        import Execute.py

print("MQTT > Starting client")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)
client.loop_forever()
