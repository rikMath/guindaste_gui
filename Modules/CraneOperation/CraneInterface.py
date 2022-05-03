import time
from Modules.CraneOperation.Coppelia.CraneSimulation import CraneSimulation


class CraneInterface:
    def __init__(self):
        self.simulation = CraneSimulation()
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
