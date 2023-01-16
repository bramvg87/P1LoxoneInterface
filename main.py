from readSerial import readSerial
from flask import Flask, jsonify

# Initialize Flask app for REST API
app = Flask(__name__)

@app.route('/P1', methods=['GET'])
def get_energy_data():
    energy_data = readSerial.readP1()
    print(energy_data)
    # Return data as JSON
    return jsonify(energy_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)