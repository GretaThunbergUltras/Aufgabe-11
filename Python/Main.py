import paho.mqtt.client as mqtt
from botlib.bot import Bot
from botlib.broker import Broker
from io import BytesIO
from brickpi3 import BrickPi3
from time import sleep
from datetime import datetime
import os

# mosquitto_pub -h 192.168.178.51 -t img_capture -m execMakePhoto

def on_connect(client, userdata, flags, rc):
    print("MQTT > Connected with result code " + str(rc))
    client.subscribe('img_capture')

def on_message(client, userdata, msg):
    payload = str(msg.payload)
    print("MQTT > topic\"{}\" payload=\"{}\"".format(msg.topic, payload))
    if "execMakePhoto" in payload:
        print("MQTT > Received start command")
        executeImageCapture()

def captureImage():
    # imageDate = datetime.now().strftime("%H-%M-%S")
    # fileName = "image_{}.jpg".format(imageDate)
    # print("Capturing image \"{}\"".format(fileName))
    # filePath = "../Images/{}".format(fileName)
    # bot.camera()._cam.capture(filePath)

    try:
        print("Capturing image")
        buff = BytesIO()
        bot.camera()._cam.capture(buff, format='jpeg')

        print("Sending images")
        buff.seek(0)
        broker.send_file('test_channel', buff.read())
    except Exception as ex:
        print(ex)

print("Initializing BotLib")
bot = Bot()
broker = Broker('gustav', 'gruppe11')

def executeImageCapture():
    captureImage()

    bp = BrickPi3()
    for i in range(3):
        print("Iteration {}/3".format(i + 1))

        bp.set_motor_power(bp.PORT_B, 40)
        sleep(2.0)
        bp.set_motor_power(bp.PORT_B, 0)
        sleep(0.5)
        captureImage()

try:
    print("Calibrating motors")
    bot.calibrate()

    print("Making images directory")
    if not os.path.isdir("../Images/"):
        os.mkdir("../Images/")

    print("MQTT > Starting client")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('gruppe11', 1883, 60)
    client.loop_forever()
except:
    print("Stopping Bot")
    bot.camera()._cam.stop_preview()
    bot.stop_all()
