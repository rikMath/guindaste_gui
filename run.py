import time
from Modules.CraneOperation.CraneInterface import CraneInterfaceFacade

import logging

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG)

if __name__ == "__main__":

    crane = CraneInterfaceFacade()
    # crane.move_hoist(100)
    # crane.activate_magnet()
    # time.sleep(1)
    # crane.move_hoist(0)
    # crane.activate_magnet()
    while True:
        print(crane.get_proximity())
    # crane.move_arm(90, "Sim")
    # print(crane.get_proximity())
    # crane.move_arm(45, "Sim")
    # print(crane.get_proximity())
    # crane.move_arm(60, "Sim")
    # print(crane.get_proximity())
    # crane.move_arm(-90, "Sim")
    # crane.move_crab(-100, "Sim")
    # while True:
    #     crane.move_crab(1, "Sim")
    #     # time.sleep(5)
    #     crane.move_crab(-1, "Sim")
    #     # time.sleep(5)
