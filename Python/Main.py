import brickpi3
from time import sleep

bp = brickpi3.BrickPi3()

def setMotorPower(power):
    bp.set_motor_power(bp.PORT_B, power)

def captureImage():
    print("capture")

captureImage()
for i in range(0, 3):
    setMotorPower(50)
    sleep(2.0)
    setMotorPower(0)
    sleep(0.5)
    captureImage()
