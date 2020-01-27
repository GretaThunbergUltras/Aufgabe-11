from picamera import PiCamera
import brickpi3
from time import sleep
import socket
import struct
import math

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.start_preview()

receiverIP = "192.168.43.83"
receiverPort = 32127
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bp = brickpi3.BrickPi3()

def setMotorPower(power):
    bp.set_motor_power(bp.PORT_B, power)

def captureImage():
    camera.capture("temp.jpg")
    with open("temp.jpg", "rb") as image:
        f = image.read()
        b = bytearray(f)
        byteCount = len(b)
        packageCount = math.ceil(byteCount / 4000)
        
        socket.sendto(struct.pack(">i", byteCount) + struct.pack(">i", packageCount), (receiverIP, receiverPort))
        for i in range(0, packageCount):
            packetSize = packageCount % 4000 if i == (packageCount - 1) else 4000
            packetBytes = b[(4000 * i):(4000*i + packetSize)]
            socket.sendto(struct.pack(">i", i) + struct.pack(">i", packetSize) + packetBytes, (receiverIP, receiverPort))


captureImage()
for i in range(0, 3):
    setMotorPower(50)
    sleep(2.0)
    setMotorPower(0)
    sleep(0.5)
    captureImage()
