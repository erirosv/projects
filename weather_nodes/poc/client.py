import requests
from smbus import SMBus
from bme280 import BME280
import time

# Web server settings - IP address and port number of the server Raspberry Pi
server_ip = 'your_server_raspberry_pi_ip'
server_port = 1234

# Initialize the BME280 sensor
bus = SMBus(1)
bme280_sensor = BME280(i2c_dev=bus)

def get_sensor_data():
    """
    Reading all the available data from the sensor. 
    - Temperature
    - Pressure
    - Humidity

    return: the sensor values
    """
    temperature = round(bme280_sensor.get_temperature(), 1)
    pressure = round(bme280_sensor.get_pressure(), 1)
    humidity = round(bme280_sensor.get_humidity(), 1)
    return temperature, pressure, humidity

def send_data_to_server():
    """
    Send sensor data to the server Raspberry Pi.
    """
    while True:
        try:
            temperature, pressure, humidity = get_sensor_data()

            data = {
                "temperature": temperature,
                "pressure": pressure,
                "humidity": humidity
            }

            # Send data to the server
            response = requests.post(f"http://{server_ip}:{server_port}/upload", json=data)

            if response.status_code == 200:
                print("Data sent successfully")
            else:
                print(f"Failed to send data. Status code: {response.status_code}")

        except Exception as e:
            print("Error:", str(e))

        # Adjust the delay as needed
        time.sleep(10)

if __name__ == '__main__':
    print("Sensor node started. Press Ctrl+C to exit.")
    send_data_to_server()
