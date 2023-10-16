import psycopg2
from smbus import SMBus
from bme280 import BME280
import time
import datetime
from datetime import date
import socket
import threading

# Database connection settings
db_host = '' # IP address
db_name = '' # name 
db_user = '' # user
db_password = '' # password

# Web server settings - portnumber
web_port = 8080

# Initialize the BME280 sensor
bus = SMBus(1)
bme280_sensor = BME280(i2c_dev=bus)

# Initialize the database connection
conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password
)

def get_censor_data():
    temperature = round(bme280_sensor.get_temperature(), 1)
    pressure = round(bme280_sensor.get_pressure(), 1)
    humidity = round(bme280_sensor.get_humidity(), 1)
    return temperature, pressure, humidity

# Create a cursor
cursor = conn.cursor()

def create_socket(port):
    # Create a socket
    address = ('0.0.0.0', port)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(address)
    server_socket.listen(1)
    return server_socket

def serve_webpage(client_socket):
    temperature, pressure, humidity  = get_censor_data()
    sensor_data = f'Temperature: {temperature}&deg;C, Pressure: {pressure} hPa, Humidity: {humidity}%'

    # structure for the simple web page
    html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <title>Weather Station</title>
        <meta http-equiv="refresh" content="10">
        <style>
            p {{
                font-size: 24px; /* Adjust the font size as needed */
            }}
        </style>
        </head>
        <body>
        <p>{sensor_data}</p>
        </body>
        </html>
    """
    response = f"HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {len(html)}\n\n{html}"
    client_socket.send(response.encode('utf-8'))
    client_socket.close()

def collect_sensor_data():
    while True:
        # Read the sensor and get date and time
        temperature, pressure, humidity  = get_censor_data()
        today = date.today()
        now = datetime.datetime.now().time()

        # Insert data into the database
        insert_query = """
        INSERT INTO weather_data (date, time, temperature, pressure, humidity)
        VALUES (%s, %s, %s, %s, %s);
        """
        data_to_insert = (today, now, temperature, pressure, humidity)
        cursor.execute(insert_query, data_to_insert)
        conn.commit()

        # Inform the user!
        print('Adding this data to the database:')
        print(today)
        print(now)
        print(f'Temperature: {temperature}C, Pressure: {pressure}hPa, Humidity: {humidity}%')

        # Set time for update
        # example: Wait for 10 minutes (600 seconds)
        time.sleep(10)

if __name__ == '__main__':
    server_socket = create_socket(web_port)
    web_thread = threading.Thread(target=collect_sensor_data)
    web_thread.daemon = True
    web_thread.start()

    # Main thread serves the web page
    print(f"Web server started on port {web_port}. Press Ctrl+C to exit.")
    while True:
        client_socket, _ = server_socket.accept()
        serve_webpage(client_socket)
