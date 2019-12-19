from Motor import *
from time import sleep


class PiRobot11:
    speed = 2000  # range -4096 => 4096
    motor = Motor()
    imageIndex = 0

    def driveStraight(self, timeMillis):
        self.motor.setMotorModel(self.speed, self.speed, self.speed, self.speed)
        time.sleep(timeMillis / 1000)
        self.motor.setMotorModel(0, 0, 0, 0)


robot = PiRobot11()
for i in range(0, 3):
    robot.driveStraight(2000)
    time.sleep(0.6)