import sys
import bluetooth

class CranePhisycal:
    def __init__(self):
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.arduino = sock

    def start(self):
        bd_addr = '44:17:93:F9:48:72'
        port = 1
        self.arduino.connect((bd_addr,port))

    def send_data(self, payload: str):
        sock = self.arduino

        sock.send(payload.encode())

    # def reeive_data(self, velocity: int):
    #     ...
