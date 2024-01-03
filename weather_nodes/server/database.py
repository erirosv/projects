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

    def init_cursor(self):
        return self.conn.cursor()

    def insert_query(self, temperature, humidity, pressure):
        cursor = self.init_cursor()
        today = date.today()
        now = datetime.datetime.now().time()
        insert_query = """
        INSERT INTO weather_data (date, time, temperature, pressure, humidity)
        VALUES (%s, %s, %s, %s, %s);
        """
        data_to_insert = (today, now, temperature, pressure, humidity)
        cursor.execute(insert_query, data_to_insert)
        self.conn.commit()