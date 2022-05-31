import time
from Modules.CraneOperation.CraneCreator import CraneCreator


class CraneInterfaceFacade:
    def __init__(self):
        self.simulation = CraneCreator.create_crane_operation_instance(kind="Coppelia")
        self.simulation.start()

        self.arduino = CraneCreator.create_crane_operation_instance(kind="Arduino")
        self.arduino.start()

    def move_arm(self, velocity: int) -> None:
        self.simulation.move_arm(velocity)
        self.arduino.move_arm(velocity)

    def move_crab(self, velocity: int) -> None:
        self.simulation.move_crab(velocity)
        self.arduino.move_crab(velocity)

    def move_hoist(self, velocity: int) -> None:
        self.simulation.move_hoist(velocity)
        # self.arduino.move_hoist(velocity)

    def use_magnet(self) -> None:
        self.simulation.use_magnet()
