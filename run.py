import time
from Modules.CraneOperation.CraneInterface import CraneInterfaceFacade


if __name__ == "__main__":

    crane = CraneInterfaceFacade()
    crane.move_hoist(-2)
    time.sleep(3)
    crane.move_hoist(2)
    time.sleep(3)
    crane.use_magnet()
    # crane.move_arm(10)
    # while True:
    #     crane.move_crab(1)
    #     time.sleep(5)
    #     crane.move_crab(-1)
    #     time.sleep(5)
