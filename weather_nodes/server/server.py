from flask import Flask, request, render_template

app = Flask(__name__)

received_data = []

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    print("Received data:", data)
    
    # Add the received data to the list
    received_data.append(data)
    
    return 'Data received successfully'

@app.route('/')
def index():
    # Render the HTML page with received data
    return render_template('index.html', data=received_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)
