from botlib.bot import Bot
from brickpi3 import BrickPi3
from time import sleep
from datetime import datetime
import os

print("Initializing BotLib")
bot = Bot()

print("Calibrating steering motor")
bot.calibrate()

print("Making images directory")
if not os.path.isdir("../Images/"):
    os.mkdir("../Images/")

def captureImage():
    imageDate = datetime.now().strftime("%H-%M-%S")
    print("Capturing image \"image_{}.jpg\"".format(imageDate))
    bot._camera._cam.capture("../Images/image_{}.jpg".format(imageDate))
    
# Capture first image
captureImage()

# Capture three images after driving 2 seconds each time
bp = BrickPi3()
for i in range(3):
    print("Iteration {}/3".format(i + 1))

    bp.set_motor_power(bp.PORT_B, 50)
    sleep(2.0)
    bp.set_motor_power(bp.PORT_B, 0)
    sleep(0.5)
    captureImage()

print("Stopping Bot")
bot.stop_all()
