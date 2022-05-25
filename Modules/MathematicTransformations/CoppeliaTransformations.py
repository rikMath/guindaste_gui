import time

class CoppeliaControl:
    ARM_VELOCITY = 1
    CRAB_VELOCITY = 1

    TIME_TO_COMPLETE_ARM = 10
    TIME_TO_COMPLETE_CRAB = 10

    def __init__(self, crane_simulation):
        """
            Utilizaremos o valor em graus para o braço
        """
        self.crane_simulation = crane_simulation
        self.position_arm = 0
        self.position_crab = 0

    def _calculate_velocity_and_time(self, old_position: float, new_position: float, velocity: float, time_complete: float):
        velocity_with_sign = -velocity if new_position > old_position  else velocity
        return velocity_with_sign, (new_position - old_position) / time_complete

    def _move_arm(self, new_position):
        crane_simulation = self.crane_simulation
        velocity, time = self._calculate_velocity_and_time(self.position_arm, new_position, self.ARM_VELOCITY, self.TIME_TO_COMPLETE_ARM)
        crane_simulation.move_arm(velocity)
        time.sleep(time)
        crane_simulation.move_arm(0)
        self.position_arm = new_position

    def _move_crab(self, new_position):
        crane_simulation = self.crane_simulation
        velocity, time = self._calculate_velocity_and_time(self.position_crab, new_position, self.CRAB_VELOCITY, self.TIME_TO_COMPLETE_CRAB)
        crane_simulation.move_crab(velocity)
        time.sleep(time)
        crane_simulation.move_crab(0)
        self.position_crab = new_position
