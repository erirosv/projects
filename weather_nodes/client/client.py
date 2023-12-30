import socket
import threading
from sensor import Sensor
import time

# Constant variables
PORT = 5050
SERVER = '192.168.50.12' # socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 1024
DISCONNECT = 'Disconnected'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

def send(msg):
    message = msg.encode(FORMAT)
    message_length = len(message)
    send_len = str(message_length).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    if message == DISCONNECT:
        print(f'[CONNECTION] {DISCONNECT}')
    else:
        print(client.recv(HEADER).decode(FORMAT))

def run():
    sensor = Sensor()
    switcher = True
    while switcher:
        temperature, pressure, humidity = sensor.read_sensor_data()
        data_to_send = f"{temperature}:{pressure}:{humidity}"
        send(data_to_send)
        time.sleep(10)

if __name__ == '__main__':
    run()
    send('test send ')
    send(DISCONNECT)  # Disconnect from the server
    client.close()