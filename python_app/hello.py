from flask import *
#from db_test import connect
import socket
import uuid

app = Flask(__name__)
indent = "    "

@app.route('/', methods = ['GET', 'POST', 'DELETE'])
def hello_world():
    host_ip = socket.gethostbyname(socket.gethostname())
    host_mac = hex(uuid.getnode())
    return str(host_ip) + " And the mac is: " + host_mac # + "     " + connect()

if __name__ == '__main__':
    app.run()
