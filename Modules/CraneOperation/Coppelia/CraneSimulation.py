import time
import numpy as np
from Modules.CraneOperation.Coppelia.CoppeliaSimulation import (
    CoppeliaSimulation,
    Joint,
    Magnet,
    Sensor,
)


class CraneSimulation:
    def __init__(self):
        self.simulation = CoppeliaSimulation()
        self.arm_joint = Joint("Torre_joint", is_revolution=True)
        self.hoist_joint = Joint("Ferramenta_actuator")
        self.magnect = Magnet("Link")
        self.sensor = Sensor("Sensor")

    def start(self):
        self.simulation.start()

    def move_arm(self, velocity: int):
        self.arm_joint.set_velocity(velocity)

    def move_arm_by_position(self, position: float):
        self.arm_joint.set_position(position)

    def get_arm_angle(self):
        # Retorno em Graus
        return round(np.rad2deg(self.arm_joint.get_position()), 2)

    def move_crab(self, velocity: int):
        self.crab_joint.set_velocity(velocity)

    def move_hoist(self, velocity: int):
        self.hoist_joint.set_velocity(velocity)

    def move_hoist_by_position(self, position: float):
        self.hoist_joint.set_position(position)

    def get_hoist_distance(self):
        # Retorno em Cm
        return round(self.hoist_joint.get_position(), 2)

    def turn_on(self):
        self.magnect.turn_on()

    def turn_off(self):
        self.magnect.turn_off()

    def get_proximity(self) -> float:
        return self.sensor.get_proximity()


if __name__ == "__main__":
    crane = CraneSimulation()
    print(crane.move_hoist(-10))
