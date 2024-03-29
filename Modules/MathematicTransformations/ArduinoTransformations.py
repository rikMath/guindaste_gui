import logging
from time import sleep

class ArduinoControl:
    STEPS_TO_DEGREE = 11.25
    STEPS_TO_CM = 1
    RECEIVE_BYTE_LENGTH = 19

    def __init__(self, micro, crane_app):
        self.crane_app = crane_app
        self.micro = micro
        self.position_arm = 0
        self.position_hoist = 0
        self.magnet_state = False
        self.id = 1

    def _get_payload_string(self, kind: str, **kwargs):
        """
            PADRÃO: 'id(3) autonomo(1) relé(1)	dir1(1)	motor1(5) dir2(1) motor2(5) eletroima(1)'
        """
        id = str(self.id).zfill(3)
        aut = "0"
        relay = "0"
        dir1 = "0"
        motor1 = "00000"
        dir2 = "0"
        motor2 = "00000"
        magnet = "0"


        if kind == "move_arm":
            degrees = kwargs["degrees"]

            dir1 = "1" if self.position_arm < (self.position_arm + degrees) else "0"
            steps = str(abs(int(degrees * self.STEPS_TO_DEGREE)))

            motor1 = "9999" if len(steps) > 5 else steps.zfill(5)

            self.position_arm += degrees

        elif kind == "move_hoist":
            cm = kwargs["cm"]

            dir2 = "1" if self.position_hoist < (self.position_hoist + cm) else "0"
            steps = str(abs(int(cm * self.STEPS_TO_CM)))

            motor2 = "9999" if len(steps) > 5 else steps.zfill(5)

            self.position_hoist += cm

        elif kind == "activate_magnet":
            magnet = "1" if kwargs["activate_magnet"] else "0"

            self.magnet_state = kwargs["activate_magnet"]


        self.id += 1

        logging.info(f"id: {id}")
        logging.info(f"aut: {aut}")
        logging.info(f"relay: {relay}")
        logging.info(f"dir1: {dir1}")
        logging.info(f"motor1: {motor1}")
        logging.info(f"dir2: {dir2}")
        logging.info(f"motor2: {motor2}")
        logging.info(f"magnet: {magnet}")

        return id + aut + relay + dir1 + motor1 + dir2 + motor2 + magnet + '\n'

    def _move_arm(self, new_position):
        logging.debug(f"CURRENT ARM POSITION {self.position_arm}")

        micro = self.micro
        current_payload = self._get_payload_string(kind="move_arm", degrees=new_position-self.position_arm)

        self.position_arm = new_position

        logging.info(f"Sending current payload: {current_payload}")

        micro.send_data(current_payload)
        self.receive_data()

        logging.debug(f"NEW ARM POSITION {new_position}")

    def _reset_arm(self):
        logging.debug(f"CURRENT ARM POSITION RESET TO 0.0 cm")

        self.position_arm = 0

    def _move_hoist(self, new_position):
        logging.debug(f"CURRENT HOIST POSITION {self.position_hoist}")

        micro = self.micro
        current_payload = self._get_payload_string(kind="move_hoist", cm=new_position-self.position_hoist)

        self.position_hoist = new_position

        micro.send_data(current_payload)
        self.receive_data()

        logging.debug(f"NEW HOIST POSITION {new_position}")

    def _reset_hoist(self):
        logging.debug(f"CURRENT HOIST POSITION RESET TO 0.0 cm")

        self.position_hoist = 0

    def _use_magnet(self, new_state):
        logging.debug(f"CURRENT MAGNET STATE {self.magnet_state}")

        micro = self.micro
        current_payload = self._get_payload_string(kind="activate_magnet", activate_magnet=new_state)

        micro.send_data(current_payload)
        self.receive_data()

        logging.debug(f"NEW MAGNET STATE {new_state}")

    # COMANDOS DE FEEDBACK - SOCK LISTEN #
    def treat_received_data(self, received_data):
        # Atualizar GUI
        logging.info(f"Current Received Data {received_data}")
        dist1 = received_data[4:9]
        dist2 = received_data[9:14]
        mag_bool = received_data[14]

        mean_dist = round((int(dist1) + int(dist2)) / 20, 2)

        self.crane_app.root.ids['sensor_state'].text = f"Posição Sensor: {abs(mean_dist)}"

        self.magnet_state = mag_bool == '1'

        state = "On" if self.magnet_state else "Off"

        self.crane_app.root.ids['magnet_state'].text = f"Estado Imã: {state}"

    def set_finished_data(self):
        logging.info("FINISHED DATA")
        self.crane_app.root.ids['arm_state'].text = f"Giro Braço: {self.position_arm}"
        self.crane_app.root.ids['hoist_state'].text = f"Altura Ferramenta: {self.position_hoist}"

    def is_finished(self, received_data):
        if (received_data[16] == "2" and not received_data[17] == "1") or (not received_data[16] == "1" and received_data[17] == "2"):
            return True
        return False

    def receive_data(self):
        logging.info("Flushing Bluetooth Data")
        self.micro.flush_data()
        logging.info("Receiving Bluetooth Data")

        while True:
            received_data = bytearray()

            while True:
                received_data += self.micro.receive_data()
                if len(received_data) >= self.RECEIVE_BYTE_LENGTH:
                    break

            decoded_data = received_data.decode("utf-8")
            self.treat_received_data(decoded_data)

            if self.is_finished(decoded_data):
                break

        self.set_finished_data()
