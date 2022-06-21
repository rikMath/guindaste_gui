import logging

class ArduinoControl:
    STEPS_TO_DEGREE = 1
    STEPS_TO_CM = 1

    def __init__(self, micro):
        self.micro = micro
        self.position_arm = 0
        self.position_hoist = 0
        self.magnet_state = False
        self.id = 1

    def _get_payload_string(self, kind: str, **kwargs):
        """
            PADRÃO: 'id(3) autonomo(1) relé(1)	dir1(1)	motor1(4) dir2(1) motor2(4) eletroima(1)'
        """
        id = str(self.id).zfill(3)
        aut = "0"
        relay = "0"
        dir1 = "0"
        motor1 = "0000"
        dir2 = "0"
        motor2 = "0000"
        magnet = "0"


        if kind == "move_arm":
            degrees = kwargs["degrees"]

            dir1 = "1" if self.position_arm < degrees else "0"
            steps = str(abs(int(degrees * self.STEPS_TO_DEGREE)))

            motor1 = "9999" if len(steps) > 4 else steps.zfill(4)

            self.position_arm = degrees

        elif kind == "move_hoist":
            cm = kwargs["cm"]

            dir2 = "1" if self.position_hoist < cm else "0"
            steps = str(abs(int(cm * self.STEPS_TO_CM)))

            motor2 = "9999" if len(steps) > 4 else steps.zfill(4)

            self.position_hoist = cm

        elif kind == "activate_magnet":
            magnet = "1" if kwargs["activate_magnet"] else "0"

            self.magnet_state = kwargs["activate_magnet"]


        self.id += 1

        return id + aut + relay + dir1 + motor1 + dir2 + motor2 + magnet + '\n'

    def _move_arm(self, new_position):
        logging.debug(f"CURRENT ARM POSITION {self.position_arm}")

        micro = self.micro
        current_payload = self._get_payload_string(kind="move_arm", degrees=new_position)

        micro.send_data(current_payload)

        logging.debug(f"NEW ARM POSITION {new_position}")

    def _reset_arm(self):
        logging.debug(f"CURRENT ARM POSITION RESET TO 0.0 cm")

        self.position_arm = 0

    def _move_hoist(self, new_position):
        logging.debug(f"CURRENT HOIST POSITION {self.position_hoist}")

        micro = self.micro
        current_payload = self._get_payload_string(kind="move_hoist", cm=new_position)

        micro.send_data(current_payload)

        logging.debug(f"NEW HOIST POSITION {new_position}")

    def _reset_hoist(self):
        logging.debug(f"CURRENT HOIST POSITION RESET TO 0.0 cm")

        self.position_hoist = 0

    def _use_magnet(self, new_state):
        logging.debug(f"CURRENT MAGNET STATE {self.magnet_state}")

        micro = self.micro
        current_payload = self._get_payload_string(kind="activate_magnet", activate_magnet=new_state)

        micro.send_data(current_payload)

        logging.debug(f"NEW MAGNET STATE {new_state}")
