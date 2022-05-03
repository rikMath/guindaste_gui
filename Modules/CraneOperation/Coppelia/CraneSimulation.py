import time
from Modules.CraneOperation.Coppelia.CoppeliaSimulation import CoppeliaSimulation, Joint


class CraneSimulation:
    def __init__(self):
        self.simulation = CoppeliaSimulation()
        self.arm_joint = Joint("ArmActuator", is_revolution=True)
        self.crab_joint = Joint("CrabActuator")

    def start(self):
        self.simulation.start()

    def move_arm(self, velocity: int):
        self.arm_joint.set_velocity(velocity)

    def move_crab(self, velocity: int):
        self.crab_joint.set_velocity(velocity)


if __name__ == "__main__":

    crane = CraneSimulation()
    crane.start()
    crane.move_arm(10)
    while True:
        crane.move_crab(1)
        time.sleep(5)
        crane.move_crab(-1)
        time.sleep(5)
