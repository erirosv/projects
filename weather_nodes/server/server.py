from flask import Flask, request, render_template

app = Flask(__name__)

latest_data = {}

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    print("Received data:", data)

    # Get a unique identifier for the node, e.g., its IP address
    node_identifier = request.remote_addr

    # Store the latest data for each node
    latest_data[node_identifier] = data
    
    return 'Data received successfully'

@app.route('/')
def index():
    # Render the HTML page with the latest data from each node
    return render_template('index.html', data=latest_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)
