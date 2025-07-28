from sqlalchemy import create_engine

# SQLite engine
engine = create_engine('sqlite:///weather_data.db', echo=False)
