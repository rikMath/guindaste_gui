import time
from Modules.CraneOperation.Coppelia.CoppeliaSimulation import (
    CoppeliaSimulation,
    Joint,
    Magnet,
    Sensor,
)


class CraneSimulation:
    def __init__(self):
        self.simulation = CoppeliaSimulation()
        self.arm_joint = Joint("Arm_actuator", is_revolution=True)
        self.crab_joint = Joint("Crab_actuator")
        self.hoist_joint = Joint("Hoist_actuator")
        self.magnect = Magnet("suctionPad")
        self.sensor = Sensor("Sensor")

    def start(self):
        print("client id: ", self.simulation.start())
        # self.magnect.actuate()
        # self.magnect.syscall_sensing()

    def move_arm(self, velocity: int):
        self.arm_joint.set_velocity(velocity)

    def move_crab(self, velocity: int):
        self.crab_joint.set_velocity(0.15 * velocity)

    def move_hoist(self, velocity: int):
        self.hoist_joint.set_velocity(0.2 * velocity)

    def use_magnet(self):
        self.magnect.actuate()

    def get_proximity(self):
        self.sensor.get_proximity()


# if __name__ == "__main__":

#     crane = CraneSimulation()
#     crane.start()
#     crane.move_arm(10)
#     while True:
#         crane.move_crab(1)
#         time.sleep(5)
#         crane.move_crab(-1)
#         time.sleep(5)
