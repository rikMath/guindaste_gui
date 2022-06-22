import sys
import bluetooth

class CranePhisycal:
    def __init__(self):
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.arduino = sock

    def start(self):
        bd_addr = '44:17:93:F9:48:72'
        # bd_addr = '78:37:16:45:4A:D2'
        port = 1
        # backlog = 1
        self.arduino.connect((bd_addr,port))
        # self.arduino.listen(backlog)

    def send_data(self, payload: str):
        sock = self.arduino
        sock.send(payload.encode())

    def receive_data(self):
        size = 1024
        return self.arduino.recv(size)

    def flush_data(self):
        while True:
            if not self.receive_data():
                break
