from flask import Flask, request
import uuid

class WebServer:
    def __init__(self, host, port):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.temperature = ''
        self.humidity = ''
        self.pressure = ''
        self.registered_clients = set()  # Set to store registered clients

        @self.app.route('/')
        def index():
            return self.generate_html_content()

        @self.app.route('/register', methods=['POST'])
        def register():
            data = request.get_json()
            if 'location' in data:
                client_id = str(uuid.uuid4())  # Generate a unique identifier
                location = data['location']
                self.registered_clients.add((client_id, location))
                return {'id': client_id, 'message': 'Registration successful'}
            else:
                return 'Invalid registration data', 400

    def is_registered(self, client_id, location):
        return (client_id, location) in self.registered_clients

    def update_data(self, client_id, location, temperature, pressure, humidity):
        if self.is_registered(client_id, location):
            self.temperature = temperature
            self.pressure = pressure
            self.humidity = humidity
        else:
            print(f"Unregistered client {client_id} from {location}. Ignoring sensor data.")

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
