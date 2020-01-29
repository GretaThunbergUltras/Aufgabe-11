from picamera import PiCamera
import brickpi3
from time import sleep
from datetime import datetime

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.start_preview()

bp = brickpi3.BrickPi3()

def captureImage():
    camera.capture("../Images/image_{}.jpg".format(datetime.now().strftime("%H-%M-%S")))
    
captureImage()
for i in range(0, 3):
    bp.set_motor_power(bp.PORT_B, 50)
    sleep(2.0)
    bp.set_motor_power(bp.PORT_B, 0)
    sleep(0.5)
    captureImage()
