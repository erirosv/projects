# Server/Client Weather station

This is a POC for a creating a simple server and a X amount of clients to connect. The server is hosting a webserver that displays the data from the sensors ower the local area network. The client reads sensor data and transmits it ower the LAN to the server. 


## Comming up
Adding the collected data from the server and push it to a database for long time storage and future work.

## Modify
This part of the server and client most likely needs to be chnaged to make the project work.

**server**
```python
PORT = 5050
SERVER = '192.168.50.12'
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 1024
DISCONNECT = 'Disconnected'
WEB_PORT = 8080
```

**Client**
```python
PORT = 5050
SERVER = '192.168.50.12' 
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 1024
DISCONNECT = 'Disconnected'
```