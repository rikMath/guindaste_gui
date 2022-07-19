import sys
import bluetooth
import time
import socket

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

    def receive_data(self):
        size = 1024
        return self.arduino.recv(size)

    def flush_data(self):
        time.sleep(1)
        # while True:
        #     data = self.arduino.recv(1024)
        #     if len(data) == 0:
        #         break
