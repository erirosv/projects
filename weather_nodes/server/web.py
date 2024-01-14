from flask import Flask

class WebServer:
    def __init__(self, host, port):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.temperature = ''
        self.humidity = ''
        self.pressure = ''

        @self.app.route('/')
        def index():
            return self.generate_html_content()

    def update_data(self, temperature, pressure, humidity):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity

    def generate_html_content(self):
        html_content = f"""
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
            <p>Temperature: {self.temperature}&deg;C, Pressure: {self.pressure} hPa, Humidity: {self.humidity}%</p>
            </body>
            </html>
        """
        return html_content

    def run(self):
        self.app.run(host=self.host, port=self.port)
