# This script will open a REST API to publish the data from a P1 meter
# The connectoin and parsing of the P1 meter has been modified based on a script created by Jens depuydt (https://github.com/jensdepuydt)
# This script is created by Bram Van Genabet (https://github.com/bramvg87)
# Instructions can be found here (https://bram.vangenabet.com/home-automation/connecting-p1-port-to-rpi)


from readSerial import readSerial
from flask import Flask, jsonify

# Initialize Flask app for REST API
app = Flask(__name__)

@app.route('/P1', methods=['GET'])
def get_energy_data():
    energy_data = readSerial.readP1()
    #print(energy_data)
    # Return data as JSON
    return jsonify(energy_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)