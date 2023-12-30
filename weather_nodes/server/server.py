import socket
import threading
import os
from functools import partial  # Import functools.partial
from web import WebServer
from database import Database
from dotenv import load_dotenv

# Constant variables
PORT = 5050
SERVER = '192.168.50.12'
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 1024
DISCONNECT = 'Disconnected'
WEB_PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

clients = set()
clients_lock = threading.Lock()

def manage_clients(web_server, connection, address):
    print(f'[CONNECTION]\t\t\t {address}')
    switch = True
    with clients_lock:
        clients.add(connection)

    while switch:
        message_length = connection.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            message = connection.recv(message_length).decode(FORMAT)
            if message == DISCONNECT:
                connection.send('[SERVER] Closing connection...'.encode(FORMAT))
                switch = False
            else:
                print(f'[{address}]\t {message}')
                temperature, pressure, humidity = parse_sensor_data(message)
                web_server.update_data(temperature, pressure, humidity)
                threading.Thread(target=database.insert_query, args=(temperature, humidity, pressure)).start()
                print(f'[DATABASE] inserted data to database')
                connection.send('[SERVER] Message received'.encode(FORMAT))

    with clients_lock:
        clients.remove(connection)
    connection.close()

def parse_sensor_data(data):
    temperature, pressure, humidity = data.split(':')
    return temperature, pressure, humidity

def init_server(web_server):
    server.listen()
    print(f'[SERVER IP]\t\t\t {SERVER}')
    while True:
        connection, address = server.accept()
        partial_manage_clients = partial(manage_clients, web_server)
        thread = threading.Thread(target=partial_manage_clients, args=(connection, address))
        thread.start()

if __name__ == "__main__":
    print(f'[SERVER STATUS]\t\t\t starting...')
    load_dotenv()
    database = Database(
        host=os.getenv('DATABASE_HOST'),
        name=os.getenv('DATABASE_NAME'),
        user=os.getenv('DATABASE_USER'),
        password=os.getenv('DATABASE_PASSWORD')
    )
    web_server_instance = WebServer(host=SERVER, port=WEB_PORT)
    web_server_thread = threading.Thread(target=web_server_instance.run)
    web_server_thread.start()
    init_server(web_server_instance)
    database.close()
