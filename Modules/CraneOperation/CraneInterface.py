import time
from Modules.CraneOperation.Coppelia.CraneSimulation import CraneSimulation
from Modules.CraneOperation.CraneCreator import CraneCreator

class CraneInterface:
    def __init__(self):
        self.simulation = CraneCreator.create_crane_operation_instance(kind="Coppelia")
        self.simulation.start()

    def move_arm(self, velocity: int) -> None:
        self.simulation.move_arm(velocity)

    def move_crab(self, velocity: int) -> None:
        self.simulation.move_crab(velocity)


if __name__ == "__main__":

    gui = GUI()
    gui.move_arm(10)
    while True:
        gui.move_crab(1)
        time.sleep(5)
        gui.move_crab(-1)
        time.sleep(5)
