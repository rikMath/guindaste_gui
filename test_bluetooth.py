import sys
import bluetooth

# devices = bluetooth.discover_devices(lookup_names=True)
# print(devices)

bd_addr = '44:17:93:F9:48:72'
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr,port))

sock.send('2'.encode())
