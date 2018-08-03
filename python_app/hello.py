from flask import Flask
import socket
import uuid

app = Flask(__name__)


@app.route("/")
def hello():
    host_ip = socket.gethostbyname(socket.gethostname())
    host_mac = hex(uuid.getnode())
    return str(host_ip) + " And the mac is: " + host_mac



if __name__ == "__main__":
    app.run(port=5010)