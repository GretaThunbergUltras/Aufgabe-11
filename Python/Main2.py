import paho.mqtt.client as mqtt
from botlib.bot import Bot
from brickpi3 import BrickPi3
from time import sleep
from datetime import datetime
import os

MQTT_SERVER = "localhost"
MQTT_PATH = "imageCapturing"

def on_connect(client, userdata, flags, rc):
    print("MQTT > Connected with result code {}".format(rc))
    client.subsribe(MQTT_PATH)

def on_message(client, userdata, msg):
    payload = str(msg.payload)
    print("MQTT > topic\"{}\" payload=\"{}\"".format(msg.topic, payload))
    if "execMakePhoto" in payload:
        print("MQTT > Received start command")
        executeMain()

def executeMain():
    captureImage()

    bp = BrickPi3()
    for i in range(3):
        print("Iteration {}/3".format(i + 1))

        bp.set_motor_power(bp.PORT_B, 40)
        sleep(2.0)
        bp.set_motor_power(bp.PORT_B, 0)
        sleep(0.5)
        captureImage()

def captureImage():
    imageDate = datetime.now().strftime("%H-%M-%S")
    print("Capturing image \"image_{}.jpg\"".format(imageDate))
    bot._camera._cam.capture("../Images/image_{}.jpg".format(imageDate))
    # TODO convert image to base64
    # TODO send image back via MQTT
    # TODO delete image and temp file

try:
    print("Initializing BotLib")
    bot = Bot()

    print("Calibrating motors")
    bot.calibrate()

    print("Making images directory")
    if not os.path.isdir("../Images/"):
        os.mkdir("../Images/")

    print("MQTT > Starting client")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_SERVER, 1883, 60)
    client.loop_forever()
except KeyboardInterrupt:
    print("Stopping bot")
    bot.stop_all()