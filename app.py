from flask import Flask
import os
import socket

app = Flask(__name__)

port = os.getenv('PORT')
path = os.getenv('ROUTE_PATH')
msg = os.getenv('MESSAGE')
hostname = socket.gethostname()
version = "v1.0.1"

if port is None:
    port = 3001

if path is None:
    path = "v1/foo"

if msg is None:
    msg = "Hello foo"


@app.route(f'/{path}')
def hello_world():  # put application's code here
    return {
        "message": msg,
        "hostname": hostname,
        "version": version
    }


if __name__ == '__main__':
    print(f"API is running")
    print(f"Hostname: {hostname}")
    print(f"Path: {path}")
    print(f"Port: {port}")
    print(f"Message: {msg}")
    app.run(debug=True, host='0.0.0.0', port=port)
