

class Weather:
    def __init__(self, temperature, pressure, humidity) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    @staticmethod
    def celcius_to_kelvin(self, temperature) -> float: return temperature + 273.15
    def get_altitude(self, pressure) -> float: 
        standard_sea_level_pressure = 1013.25
        return 44330 * (1 - (pressure / standard_sea_level_pressure)**0.1903)

    def sea_level_pressure(self, temperature=288.15, lapse_rate=0.0065):
        altitude = self.get_altitude()
        kelvin = self.celsius_to_kelvin(temperature)
        sea_level_pressure = 101325  # Standard atmospheric pressure at sea level in Pascals
        # Calculate pressure using the barometric formula
        pressure = sea_level_pressure * (1 - (lapse_rate * altitude) / kelvin) ** (1 / lapse_rate)
        return pressure

    