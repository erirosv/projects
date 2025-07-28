import requests
import pandas as pd
from datetime import datetime
import os
from config import API_KEY, CITY, UNITS
from database import engine

# API URL for current weather
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}"

def fetch_weather():
    try:
        # Call the OpenWeatherMap API
        response = requests.get(URL)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        # Extract and structure weather data
        weather = {
            'city': CITY,
            'timestamp': datetime.utcnow(),
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'weather': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed']
        }

        # Convert to DataFrame
        df = pd.DataFrame([weather])

        # Store in SQLite database
        df.to_sql('weather', engine, if_exists='append', index=False)

        # Optional: also log to CSV
        csv_path = 'weather_log.csv'
        write_header = not os.path.exists(csv_path)
        df.to_csv(csv_path, mode='a', header=write_header, index=False)

        print(f"Stored weather data at {weather['timestamp']}")

    except Exception as e:
        print(f"Error fetching weather: {e}")

if __name__ == "__main__":
    fetch_weather()
