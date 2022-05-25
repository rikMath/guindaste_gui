import time
from Modules.CraneOperation.CraneInterface import CraneInterfaceFacade


if __name__ == "__main__":

    crane = CraneInterfaceFacade()
    crane.move_arm(10, "Sim")
    while True:
        crane.move_crab(1, "Sim")
        time.sleep(5, "Sim")
        crane.move_crab(-1, "Sim")
        time.sleep(5, "Sim")
