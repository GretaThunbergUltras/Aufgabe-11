from Motor import *
from picamera import PiCamera
from time import sleep


class PiRobot11:
    speed = 2000  # range -4096 => 4096
    motor = Motor()
    camera = PiCamera()
    camera.resolution = (1920, 1080)
    camera.start_preview()
    imageIndex = 0

    def driveStraight(self, timeMillis):
        self.motor.setMotorModel(self.speed, self.speed, self.speed, self.speed)
        time.sleep(timeMillis / 1000)
        self.motor.setMotorModel(0, 0, 0, 0)

    def makePhoto(self, number):
        camera.capture("picture{}.jpg".format(number))


robot = PiRobot11()
robot.makePhoto(0)
for i in range(0, 3):
    robot.driveStraight(2000)
    time.sleep(0.6)
    robot.makePhoto(i + 1)
