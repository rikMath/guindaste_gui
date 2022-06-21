import sys
import bluetooth

# devices = bluetooth.discover_devices(lookup_names=True)
# print(devices)

bd_addr = '78:37:16:45:4A:D2'
port = bluetooth.PORT_ANY
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr,port))

sock.send('2'.encode())
