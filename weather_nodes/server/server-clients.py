#!/usr/bin/env python3

import socket
import threading
import os
import sys
from functools import partial
from weather_nodes.server.web1 import WebServer
from database import Database
from weather import Weather
from dotenv import load_dotenv
import signal

# Constant variables
PORT = 5050
SERVER = '192.168.50.12'
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 1024
DISCONNECT = 'Disconnected'
WEB_PORT = 8080

threads_lock = threading.Lock()

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
            elif message.lower() == 'q':
                message = connection.recv(message_length).decode(FORMAT)
            else:
                print(f'[{address}]\t {message}')
                id_name, location, temperature, pressure, humidity = parse_sensor_data(message)
                pressure = Weather.sea_level_pressure(temperature, pressure, humidity)
                web_server.update_data(temperature, pressure, humidity, id_name, location)
                threading.Thread(target=database.insert_query, args=(temperature, humidity, pressure, id_name, location)).start()
                print(f'[DATABASE] inserted data to database')
                connection.send('[SERVER] Message received'.encode(FORMAT))

    with clients_lock:
        clients.remove(connection)
    connection.close()

def parse_sensor_data(data):
    id_name, location, temperature, pressure, humidity = data.split(':')
    return id_name, location, temperature, pressure, humidity

def init_server(web_server):
    threads = []
    try:
        signal.signal(signal.SIGINT, lambda signum, frame: shutdown_server(web_server, threads))

        server.listen()
        print(f'[SERVER IP]\t\t\t {SERVER}')
        threads = []

        while True:
            connection, address = server.accept()
            partial_manage_clients = partial(manage_clients, web_server)
            thread = threading.Thread(target=partial_manage_clients, args=(connection, address))
            thread.start()
            threads.append(thread)

    except KeyboardInterrupt:
        print("Server stopped by user. Cleaning up...")
        server.close()

        for thread in threads:
            try:
                thread.join()
            except KeyboardInterrupt:
                pass  # Ignore additional KeyboardInterrupt during thread.join()

        # Perform any additional cleanup if needed
        print("Server and threads successfully stopped.")
        sys.exit()

    except SystemExit:
        # Catch SystemExit and do nothing to allow a graceful exit
        pass 

def shutdown_server(web_server, threads):
    with threads_lock:
        # Access and modify the threads list within the lock
        for thread in threads:
            try:
                thread.join()
            except KeyboardInterrupt:
                pass  # Ignore additional KeyboardInterrupt during thread.join()

    # Perform any additional cleanup if needed
    print("Server and threads successfully stopped.")
    sys.exit()

if __name__ == "__main__":
    print(f'[SERVER STATUS]\t\t\t starting...')
    load_dotenv()
    print(f'[SERVER STATUS]\t\t\t Database connection initializing...')
    
    with Database(
        host=os.getenv('DATABASE_HOST'),
        name=os.getenv('DATABASE_NAME'),
        user=os.getenv('DATABASE_USER'),
        password=os.getenv('DATABASE_PASSWORD')
    ) as database:
        print(f'[SERVER STATUS]\t\t\t Database connection accepted')
        print(f'[SERVER STATUS]\t\t\t Webserver initializing...')
        web_server_instance = WebServer(host=SERVER, port=WEB_PORT, database=database)
        web_server_thread = threading.Thread(target=web_server_instance.run)
        web_server_thread.start()
        print(f'[SERVER STATUS]\t\t\t Webserver {SERVER}:{WEB_PORT}')
        init_server(web_server_instance)
