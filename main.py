from flask import Flask
from flask import jsonify

app = Flask(__name__)

machines_list = [
    {'ipaddr':'127.0.0.1', 'ostype': 'windows'},
    {'ipaddr':'192.168.0.101', 'ostype': 'linux'}
]

# POST request for adding new machine
@app.route('/addmachine/',methods=['POST'])
def add_machine():
    pass

#Get request for list of machines added
@app.route('/getmachines/')
def get_machines():
    return jsonify(machines_list)

@app.route('/machine/mem/')
def check_mem():
    machineip = '127.0.0.1'




if __name__ == '__main__':
    app.run(port=5000,debug=True)