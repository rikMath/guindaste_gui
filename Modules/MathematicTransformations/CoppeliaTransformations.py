import time
from threading import Timer
import logging


class CoppeliaControl:
    ARM_VELOCITY = 2
    HOIST_VELOCITY = 1

    TIME_TO_COMPLETE_ARM = 70
    TIME_TO_COMPLETE_HOIST = 10

    def __init__(self, crane_simulation, crane_app):
        """
        Utilizaremos o valor em graus para o braço
        """
        self.crane_simulation = crane_simulation
        self.crane_app = crane_app
        self.position_arm = 0
        self.position_hoist = 0
        self.magnet_state = False

    def _calculate_velocity_and_time(
        self,
        old_position: float,
        new_position: float,
        velocity: float,
        time_complete: float,
    ):

        velocity_with_sign = -velocity if new_position > old_position else velocity
        return velocity_with_sign, abs(
            (new_position - old_position) * time_complete / 360
        )

    def _move_arm(self, new_position):
        logging.info(f"CURRENT ARM POSITION {self.position_arm}")

        crane_simulation = self.crane_simulation
        velocity, time_sleep = self._calculate_velocity_and_time(
            self.position_arm,
            new_position,
            self.ARM_VELOCITY,
            self.TIME_TO_COMPLETE_ARM,
        )

        logging.info(f"Moving Arm with velocity {velocity} for {time_sleep} seconds")
        crane_simulation.move_arm(velocity)

        logging.info("ARM STARTED TO MOVE")
        self._sleep(time_sleep)

        logging.info("ARM FINISHED TO MOVE")
        crane_simulation.move_arm(0)

        self.position_arm = new_position

        logging.info(f"NEW ARM POSITION {new_position}")

    def _reset_arm(self):
        logging.info(f"CURRENT ARM POSITION RESET TO 0.0 Degrees")

        self.position_arm = 0

    def _move_hoist(self, new_position):
        logging.info(f"CURRENT HOIST POSITION {self.position_hoist}")

        crane_simulation = self.crane_simulation
        velocity, time_sleep = self._calculate_velocity_and_time(
            self.position_hoist,
            new_position,
            self.HOIST_VELOCITY,
            self.TIME_TO_COMPLETE_HOIST,
        )

        logging.info(f"Moving Crab with velocity {velocity} for {time_sleep} seconds")

        logging.info("HOIST STARTED TO MOVE")
        crane_simulation.move_hoist(velocity)

        logging.info("HOIST FINISHED TO MOVE")
        self._sleep(time_sleep)
        crane_simulation.move_hoist(0)

        self.position_hoist = new_position
        logging.info(f"NEW HOIST POSITION {new_position}")

    def _reset_hoist(self):
        logging.info(f"CURRENT HOIST POSITION RESET TO 0.0 cm")

        self.position_hoist = 0

    def _use_magnet(self, new_state: bool):
        crane_simulation = self.crane_simulation

        if new_state and not self.magnet_state:
            crane_simulation.use_magnet()
        if not new_state and self.magnet_state:
            crane_simulation.use_magnet()

        crane_simulation.use_magnet()

        self.magnet_state = new_state

    def _thread_sleep_auxiliar(self, remaining_seconds):
        ...

    def _sleep(self, seconds):
        int_seconds = int(seconds)
        for _ in range(int_seconds):
            logging.info(f"PROXIMITY SENSOR: {self.crane_simulation.get_proximity()}")
            time.sleep(1)
        time.sleep(seconds - int_seconds)
