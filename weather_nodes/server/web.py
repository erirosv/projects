# In web.py
from flask import Flask, request, render_template_string
import uuid

class WebServer:
    def __init__(self, host, port, database):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.temperature = ''
        self.humidity = ''
        self.pressure = ''
        self.database = database

        # Initialize registered clients from the database
        self.registered_clients = self.database.get_registered_clients()

        @self.app.route('/')
        def index():
            return self.generate_html_content()

        @self.app.route('/register', methods=['GET', 'POST'])
        def register():
            if request.method == 'POST':
                data = request.get_json()
                if 'location' in data:
                    location = data['location']

                    # If there are no registered clients, generate an ESP32 ID with the number 1
                    if not self.registered_clients:
                        client_id = "ESP32_1"
                    else:
                        # Find the next available number for ESP32 ID
                        max_client_number = max(int(client_id.split('_')[1]) for client_id, _ in self.registered_clients)
                        next_client_number = max_client_number + 1
                        client_id = f"ESP32_{next_client_number}"

                    # Update registered clients in the database
                    self.database.insert_registered_client(client_id, location)

                    self.registered_clients.add((client_id, location))
                    return {'id': client_id, 'message': 'Registration successful'}
                else:
                    return 'Invalid registration data', 400
            else:
                # Use the provided HTML code for the registration form
                return render_template_string("""
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <title>Register Form</title>
                    </head>
                    <body>
                        <form action="{{ url_for('register') }}" method="post" enctype="application/json">
                            <!-- Replace the input with a dropdown menu for ESP32 ID -->
                            <label for="id">ESP32 ID:</label>
                            <select id="id" name="id" required>
                                {% for client in existing_clients %}
                                <option value="{{ client.client_id }}">{{ client.location }}</option>
                                {% endfor %}
                            </select>

                            <!-- Add the required attribute for the "Location" input -->
                            <label for="location">Location:</label>
                            <input type="text" id="location" name="location" required>

                            <button type="submit">Register</button>
                        </form>
                    </body>
                    </html>
                """)

    def find_next_id(self):
        # Find the next available ESP32 ID
        existing_ids = {int(client.client_id.split('_')[1]) for client in self.registered_clients if '_' in client.client_id}
        next_id = 1
        while next_id in existing_ids:
            next_id += 1
        return f'esp32_{next_id}'
            
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
