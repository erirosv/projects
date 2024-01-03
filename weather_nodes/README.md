# Server/Client Weather station

This is a POC for a creating a simple server and a X amount of clients to connect. The server is hosting a webserver that displays the data from the sensors ower the local area network. The client reads sensor data and transmits it ower the LAN to the server. 

## TODO
- [ ] Restart the database and add all the columns needed
    - [ ] Simple database model
- [ ] Add the extra columns from database to code
- [ ] Testing 

## Content
Server:
- server
- web server
- database

Client:
- client
- sensor

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

**Database**
This is the needed variables for teh postgres DB, they are stored in a .env file for security.

```python
DATABASE_NAME = ''
DATABSE_USER = ''
DATABASE_ADDRESS = ''
DATABASE_PASSWORD = ''
```