from readSerial import readSerial
from flask import Flask, jsonify

# Initialize Flask app for REST API
app = Flask(__name__)

@app.route('/P1', methods=['GET'])
def get_energy_data():
    # Read data from P1 energy meter
    #data = ser.readline().decode('utf-8')

    # Use regular expressions to parse data
    #match = re.search("(?P<power>[0-9.]+) kW", data)
    #power = float(match.group("power"))

    energy_data = readSerial.readP1()
    print(energy_data)
    # Return data as JSON
    return jsonify(energy_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)