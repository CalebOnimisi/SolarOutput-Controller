from flask import Flask, request, jsonify
from flask_cors import CORS
import util

util_path = "util.py"

app = Flask(__name__)
CORS(app)

# Initialize values to be used if no data is received
office = 0
lab = 0
val1 = 0
val2 = 0
val3 = 0

@app.route('/receive_state', methods=['POST'])
def receive_state():
    global office, lab
    try:
        received_state = request.get_json()
        print("Received state:", received_state)  # Add this line to print the received data

        if 'office0' in received_state:
            office = received_state['office0']
            print(f"Received office0: {office}")

        if 'lab0' in received_state:
            lab = received_state['lab0']
            print(f"Received lab0: {lab}")

        return "Data received successfully", 200
    except Exception as e:
        return f"Error: {str(e)}", 400

@app.route('/send_data', methods=['POST'])
def receive_data():
    global val1, val2, val3
    try:
        received_data = request.get_json()
        print("Received data:", received_data)  # Add this line to print the received data

        if 'result1' in received_data and 'result2' in received_data and 'result3' in received_data:
            val1 = received_data['result1']
            val2 = received_data['result2']
            val3 = received_data['result3']
            print(f"Received result1: {val1}, result2: {val2}, result3: {val3}")

            return "Data received successfully", 200
        else:
            return "Invalid data format", 400
    except Exception as e:
        return f"Error: {str(e)}", 400

@app.route('/gas_state', methods=['GET'])
def predict_user_input():
    try:
        global val1, val2, val3
        # Use the received values or default values if not received
        input1 = val1
        input2 = val2
        input3 = val3

        # Call the utility function to make predictions
        result = util.predict_user_input(input1, input2, input3)
        # Construct the response
        response = jsonify({
            'result': result
        })

        return response

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
