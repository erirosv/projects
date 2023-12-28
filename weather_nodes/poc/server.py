from flask import Flask, request, render_template

app = Flask(__name__)

latest_data = {}

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    node_identifier = request.remote_addr  # Use the IP address of the sender as an identifier

    latest_data[node_identifier] = data
    print(f"Received data from {node_identifier}: {data}")

    return 'Data received successfully'

@app.route('/')
def index():
    return render_template('index.html', data=latest_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)
