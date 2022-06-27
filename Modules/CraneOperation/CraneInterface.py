import time
from Modules.CraneOperation.CraneCreator import CraneCreator
from Modules.MathematicTransformations import CoppeliaControl, ArduinoControl

import logging


class CraneInterfaceFacade:
    def __init__(self, run_kind, crane_app):
        if run_kind == "Sim" or run_kind == "Both":
            self.simulation = sim = CraneCreator.create_crane_operation_instance(
                kind="Coppelia"
            )
            sim.start()
        else:
            self.simulation = sim = None

        self.simulation_control = CoppeliaControl(sim, crane_app)

        if run_kind == "Micro" or run_kind == "Both":
            self.arduino = micro = CraneCreator.create_crane_operation_instance(
                kind="Arduino"
            )
            micro.start()
        else:
            self.arduino = micro = None

        self.arduino_control = ArduinoControl(micro, crane_app)

        self._runner = {
            "Sim": self.simulation_control,
            "Micro": self.arduino_control,
            "Both": self,
        }

    # Chamadas internas

    def _move_arm(self, degree):
        self.arduino_control._move_arm(degree)
        self.simulation_control._move_arm(degree)

    def _move_hoist(self, distance):
        self.arduino_control._move_hoist(distance)
        self.simulation_control._move_hoist(distance)

    def _reset_arm(self):
        self.arduino_control._reset_arm()
        self.simulation_control._reset_arm()

    def _reset_hoist(self):
        self.arduino_control._reset_hoist()
        self.simulation_control._reset_hoist()

    # Interfaces de comandos

    def move_arm(self, degree: float, kind="Sim") -> None:
        logging.info(f"Moving ARM -> {degree} degrees")
        self._runner[kind]._move_arm(degree)
        logging.info(f"ARM MOVED -> {degree} degrees")

    def reset_arm(self, kind="Sim") -> None:
        logging.info(f"RESETING ARM VALUE")
        self._runner[kind]._reset_arm()

    def reset_hoist(self, kind="Sim") -> None:
        logging.info(f"RESETING ARM VALUE")
        self._runner[kind]._reset_hoist()

    # def move_hoist(self, velocity: int) -> None:
    #     self.simulation.move_hoist(velocity)
    #     self.arduino.move_hoist(velocity)
    #
    # def move_hoist(self, velocity: int) -> None:
    #     self.simulation.move_hoist(velocity)
    #     # self.arduino.move_hoist(velocity)

    def get_proximity(self) -> float:
        return self.simulation.get_proximity()

    def move_hoist(self, distance: int, kind="Sim") -> None:
        logging.info(f"Moving hoist -> {distance} cm")
        self._runner[kind]._move_hoist(distance)
        logging.info(f"hoist MOVED -> {distance} cm")

    def activate_magnet(self, kind="Sim"):
        logging.info(f"ACTIVATING MAGNET")
        self._runner[kind]._use_magnet(True)
        logging.info(f"MAGNET ACTIVATED")

    def deactivate_magnet(self, kind="Sim"):
        logging.info(f"DEACTIVATING MAGNET")
        self._runner[kind]._use_magnet(False)
        logging.info(f"MAGNET DEACTIVATED")
