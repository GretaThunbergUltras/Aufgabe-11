from lib.Motor import *
from time import sleep
from picamera import PiCamera


class PiRobot11:
    speed = 2000  # range -4096 => 4096
    motor = Motor()
    piCamera = None
    imageIndex = 0

    def initCamera(self):
        self.piCamera = PiCamera()
        self.piCamera.resolution = (1920, 1080)
        time.sleep(3)

    def driveStraight(self, timeMillis):
        self.motor.setMotorModel(self.speed, self.speed, self.speed, self.speed)
        time.sleep(timeMillis / 1000)
        self.motor.setMotorModel(0, 0, 0, 0)

    def captureImage(self):
        self.imageIndex = 0
        self.piCamera.capture("image-{}.jpeg".format(self.imageIndex))
        self.imageIndex += 1
        pass


robot = PiRobot11()
robot.initCamera()
robot.captureImage()
for i in range(0, 3):
    robot.driveStraight(2000)
    robot.captureImage()