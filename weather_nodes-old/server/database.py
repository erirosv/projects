#!/usr/bin/env python3

import psycopg2
from datetime import date
import datetime

class Database:
    def __init__(self, host, name, user, password):
        self.db_host = host
        self.db_name = name
        self.db_user = user
        self.db_password = password

        self.conn = psycopg2.connect(
            host=self.db_host,
            database=self.db_name,
            user=self.db_user,
            password=self.db_password
        )
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def init_cursor(self):
        return self.conn.cursor()

    def insert_query(self, client_id, location, temperature, humidity, pressure):
        with self:
            cursor = self.init_cursor()
            today = date.today()
            now = datetime.datetime.now().time()
            insert_query = """
            INSERT INTO weather_data (client_id, date, time, temperature, pressure, humidity)
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            data_to_insert = (client_id, today, now, temperature, pressure, humidity)
            cursor.execute(insert_query, data_to_insert)
            self.conn.commit()