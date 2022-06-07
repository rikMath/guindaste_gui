import time
from Modules.CraneOperation.CraneCreator import CraneCreator
from Modules.MathematicTransformations import CoppeliaControl, ArduinoControl

import logging


class CraneInterfaceFacade:
    def __init__(self):
        self.simulation = sim = CraneCreator.create_crane_operation_instance(
            kind="Coppelia"
        )
        sim.start()

        self.simulation_control = CoppeliaControl(sim)

        self.arduino = micro = CraneCreator.create_crane_operation_instance(
            kind="Arduino"
        )
        micro.start()

        self.arduino_control = ArduinoControl(micro)

        self._runner = {
            "Sim": self.simulation_control,
            "Micro": self.arduino_control,
            "Both": self,
        }

    # Chamadas internas

    def _move_arm(self, degree):
        self.arduino_control._move_arm(degree)
        self.simulation_control._move_arm(degree)

    def _move_crab(self, distance):
        self.arduino_control._move_crab(distance)
        self.simulation_control._move_crab(distance)

    def _reset_arm(self):
        self.arduino_control._reset_arm()
        self.simulation_control._reset_arm()

    # Interfaces de comandos

    def move_arm(self, degree: float, kind="Sim") -> None:
        logging.info(f"Moving ARM -> {degree} degrees")
        self._runner[kind]._move_arm(degree)
        logging.info(f"ARM MOVED -> {degree} degrees")

    def reset_arm(self, kind="Sim") -> None:
        logging.info(f"RESETING ARM VALUE")
        self._runner[kind]._reset_arm()

    def move_crab(self, velocity: int) -> None:
        self.simulation.move_crab(velocity)
        self.arduino.move_crab(velocity)

    def move_hoist(self, velocity: int) -> None:
        self.simulation.move_hoist(velocity)
        # self.arduino.move_hoist(velocity)

    def use_magnet(self) -> None:
        self.simulation.use_magnet()


    def get_proximity(self) -> None:
        self.simulation.get_proximity()

    def move_crab(self, distance: int, kind="Sim") -> None:
        logging.info(f"Moving CRAB -> {distance} cm")
        self._runner[kind]._move_crab(distance)
        logging.info(f"CRAB MOVED -> {distance} cm")
