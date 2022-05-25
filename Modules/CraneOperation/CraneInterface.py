import time
from Modules.CraneOperation.CraneCreator import CraneCreator
from Modules.MathematicTransformations import CoppeliaControl, ArduinoControl

class CraneInterfaceFacade:

    def __init__(self):
        self.simulation = sim = CraneCreator.create_crane_operation_instance(kind="Coppelia")
        sim.start()

        self.simulation_control = CoppeliaControl(sim)

        self.arduino = sim = CraneCreator.create_crane_operation_instance(kind="Arduino")
        sim.start()

        self.arduino_control = ArduinoControl(sim)

        self._runner = {
            "Sim": self.simulation_control,
            "Micro": self.arduino_control,
            "Both": self,
        }

    def _move_arm(self, degree):
        self.arduino_control._move_arm(velocity)
        self.simulation_control._move_arm(degree)

    def _move_crab(self, distance):
        self.arduino_control._move_crab(velocity)
        self.simulation_control._move_crab(degree)

    def move_arm(self, degree: float, kind="Sim") -> None:
        self._runner[kind]._move_arm(degree)

    def move_crab(self, distance: int, kind="Sim") -> None:
        self._runner[kind]._move_arm(distance)
