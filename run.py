import time
from Modules.CraneInterface import CraneInterface


if __name__ == "__main__":

    crane = CraneInterface()
    crane.move_arm(10)
    while True:
        crane.move_crab(1)
        time.sleep(5)
        crane.move_crab(-1)
        time.sleep(5)
