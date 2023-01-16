#ChatGPT Instructions: 
# Please write python code to run on a raspberry pi, 
# Read data from a P1 energy meter from the usb serial port, 
# parse the data using regex and publish the data using a simple REST API server via a json.

import serial
import re
from flask import Flask, jsonify

# Open serial connection to P1 energy meter
#ser = serial.Serial('/dev/ttyUSB0', 9600)




# Initialize Flask app for REST API
app = Flask(__name__)

@app.route('/P1', methods=['GET'])
def get_energy_data():
    # Read data from P1 energy meter
    #data = ser.readline().decode('utf-8')

    # Use regular expressions to parse data
    #match = re.search("(?P<power>[0-9.]+) kW", data)
    #power = float(match.group("power"))

    power = 123
    # Return data as JSON
    return jsonify(power=power)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)