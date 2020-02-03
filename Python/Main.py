import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code"+str(rc))
    client.subscribe(MQTT_PATH)


def on_message(client, userdata, msg):
    payload = str(msg.payload)
    print(msg.topic+" "+str(payload))
    print("execMakePhoto" in payload)
    if "execMakePhoto" in payload:
        import Execute.py
    

try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_SERVER, 1883, 60)

    client.loop_forever()
except KeyboardInterrupt:
    print("STOP!!!")