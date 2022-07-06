import time
from threading import Timer
import logging

from kivy.clock import Clock

class CoppeliaControl:
    ARM_VELOCITY = 1
    HOIST_VELOCITY = 1

    TIME_TO_COMPLETE_ARM = 75
    TIME_TO_COMPLETE_HOIST = 6

    def __init__(self, crane_simulation, crane_app):
        """
        Utilizaremos o valor em graus para o braço
        """
        self.crane_simulation = crane_simulation
        self.crane_app = crane_app
        self.position_arm = 0
        self.position_hoist = 0
        self.magnet_state = False

        if crane_simulation:
            Clock.schedule_interval(self.treat_coppelia_data, 1)

    def _calculate_velocity_and_time_arm(
        self,
        old_position: float,
        new_position: float,
        velocity: float,
        time_complete: float,
    ):

        velocity_with_sign = -velocity if new_position > old_position else velocity
        return velocity_with_sign, abs((new_position - old_position) / 360 * time_complete)
        # return velocity_with_sign, abs((new_position - old_position) * time_complete)

    def _calculate_velocity_and_time_hoist(
        self,
        old_position: float,
        new_position: float,
        velocity: float,
        time_complete: float,
    ):

        velocity_with_sign = -velocity if new_position > old_position else velocity
        return -velocity_with_sign, abs((new_position - old_position) / 27 * time_complete)

    def _move_arm(self, new_position):
        logging.info(f"CURRENT ARM POSITION {self.position_arm}")

        crane_simulation = self.crane_simulation
        velocity, time_sleep = self._calculate_velocity_and_time_arm(
            self.position_arm,
            new_position,
            self.ARM_VELOCITY,
            self.TIME_TO_COMPLETE_ARM,
        )

        logging.info(f"Moving Arm with velocity {velocity} for {time_sleep} seconds")
        crane_simulation.move_arm(new_position)

        logging.info("ARM STARTED TO MOVE")
        self.treat_coppelia_data()

        logging.info("ARM FINISHED TO MOVE")
        # crane_simulation.move_arm(0)

        self.position_arm = new_position

        logging.info(f"NEW ARM POSITION {new_position}")

    def _reset_arm(self):
        logging.info(f"CURRENT ARM POSITION RESET TO 0.0 Degrees")

        self.position_arm = 0

    def _move_hoist(self, new_position):
        logging.info(f"CURRENT HOIST POSITION {self.position_hoist}")

        if new_position >= 27:
            new_position = 27

        crane_simulation = self.crane_simulation
        velocity, time_sleep = self._calculate_velocity_and_time_hoist(
            self.position_hoist,
            new_position,
            self.HOIST_VELOCITY,
            self.TIME_TO_COMPLETE_HOIST,
        )

        logging.info(f"Moving Crab with velocity {velocity} for {time_sleep} seconds")

        logging.info("HOIST STARTED TO MOVE")
        crane_simulation.move_hoist(new_position/10)

        logging.info("HOIST FINISHED TO MOVE")
        self.treat_coppelia_data()

        self.position_hoist = new_position
        logging.info(f"NEW HOIST POSITION {new_position}")

    def _reset_hoist(self):
        logging.info(f"CURRENT HOIST POSITION RESET TO 0.0 cm")

        self.position_hoist = 0

    def _use_magnet(self, new_state: bool):
        crane_simulation = self.crane_simulation

        if new_state and not self.magnet_state:
            crane_simulation.turn_on()
        if not new_state and self.magnet_state:
            crane_simulation.turn_off()

        self.magnet_state = new_state

        self.treat_coppelia_data()

    def treat_coppelia_data(self, dt=None):
        root = self.crane_app.root

        new_arm_position = self.crane_simulation.get_arm_angle()
        new_hoist_position = self.crane_simulation.get_hoist_distance()
        new_sensor_position = self.crane_simulation.get_proximity()

        root.ids["arm_state"].text = f"Giro Braço: {round(abs(new_arm_position)%360, 2)}"
        root.ids["hoist_state"].text = f"Altura Ferramenta: {round(abs(new_hoist_position*10), 2)}"
        root.ids["sensor_state"].text = f"Posição Sensor: {round(abs(new_sensor_position)*10, 2)}"
        state = "On" if self.magnet_state else "Off"
        root.ids["magnet_state"].text = f"Estado Imã: {state}"

        logging.info(f"Arm -> {new_arm_position} degrees, {root.ids['arm_state'].text}")
        logging.info(f"Hoist -> {new_arm_position} cm, {root.ids['hoist_state'].text}")
        logging.info(f"Sensor -> {new_sensor_position} cm, {root.ids['sensor_state'].text}")
