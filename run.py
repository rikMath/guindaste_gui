import time
from Modules.CraneOperation.CraneInterface import CraneInterfaceFacade
from Modules.CraneOperation.Coppelia.CraneSimulation import CraneSimulation
import logging

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG)


if __name__ == "__main__":
    crane = CraneSimulation()
    options_gui = {
        "1": {"input": "Target degree: ", "call": crane.move_arm},
        "2": {"input": "Target High: ", "call": crane.move_hoist},
    }
    crane.start()

    while True:
        choose = input("1 - Move Arm \n2 - Move Hoist\n3 - ON\n4 - OFF\nOption: ")
        try:
            if choose == "3":
                crane.turn_on()
            elif choose == "4":
                crane.turn_off()
            else:
                options_gui.get(choose).get("call")(
                    float(input(options_gui.get(choose).get("input")))
                )
        except:
            print("Option not allowed")

        # print(crane.get_proximity())
    # print(crane.move_arm(180))
    # print(crane.move_arm(-90))

    # crane = CraneInterfaceFacade("Sim", "hi")
    # # crane.move_hoist(100)
    # # crane.activate_magnet()
    # # time.sleep(1)
    # crane.move_hoist(-300)
    # # crane.activate_magnet()
    # # for _ in range(10):
    # #     time.sleep(60)
    # #     print(crane.get_proximity())

    # crane.move_hoist(300)
    # crane.activate_magnet()
    # crane.move_hoist(-300)
    # crane.move_hoist(300)
    # crane.activate_magnet()
    # while True:
    #     print(crane.get_proximity())
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
