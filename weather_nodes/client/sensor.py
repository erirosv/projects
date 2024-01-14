#! bin/bash/env python3 

from smbus import SMBus
from bme280 import BME280
import time
import datetime
from datetime import date

bus = SMBus(1)
bme280_sensor = BME280(i2c_dev=bus)

class Sensor:
    def __init__(self):
        self.temperature = 0.0  
        self.humidity = 0.0
        self.pressure = 0.0

    def read_sensor_data(self):
        self.temperature = round(bme280_sensor.get_temperature(), 1)
        self.pressure = round(bme280_sensor.get_pressure(), 1)
        self.humidity = round(bme280_sensor.get_humidity(), 1)
        return self.temperature, self.pressure, self.humidity