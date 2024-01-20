# In web.py
from flask import Flask, request, render_template_string, render_template
import uuid

class WebServer:
    def __init__(self, host, port, database):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.database = database
        self.temperature = ''
        self.humidity = ''
        self.pressure = ''
        self.location = ''
        self.node_data = {}


        # Initialize registered clients from the database
        self.registered_clients = self.database.get_registered_clients()

        @self.app.route('/')
        def index():
            return render_template('index.html', temperature=self.temperature, pressure=self.pressure, humidity=self.humidity, node_data=self.node_data)

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
                return render_template('register.html')

    def find_next_id(self):
        # Find the next available ESP32 ID
        existing_ids = {int(client.client_id.split('_')[1]) for client in self.registered_clients if '_' in client.client_id}
        next_id = 0 
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
            self.location = location
        else:
            print(f"Unregistered client {client_id} from {location}. Ignoring sensor data.")

    def run(self):
        self.app.run(host=self.host, port=self.port)
