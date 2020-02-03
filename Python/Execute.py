from botlib.bot import Bot
from brickpi3 import BrickPi3
from time import sleep
from datetime import datetime
import os

def captureImage():
    imageDate = datetime.now().strftime("%H-%M-%S")
    fileName = "image_{}.jpg".format(imageDate)
    print("Capturing image \"{}\"".format(fileName))
    filePath = "../Images/{}".format(fileName)
    bot._camera._cam.capture(filePath)
    # TODO convert image to base64
    # TODO send image back via MQTT
    # TODO delete image and temp file

print("Initializing BotLib")
bot = Bot()

print("Calibrating motors")
bot.calibrate()

print("Making images directory")
if not os.path.isdir("../Images/"):
    os.mkdir("../Images/")

captureImage()

bp = BrickPi3()
for i in range(3):
    print("Iteration {}/3".format(i + 1))

    bp.set_motor_power(bp.PORT_B, 40)
    sleep(2.0)
    bp.set_motor_power(bp.PORT_B, 0)
    sleep(0.5)
    captureImage()
