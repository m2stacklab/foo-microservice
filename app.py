from flask import Flask
import os

app = Flask(__name__)

PORT = os.getenv('PORT')
FOO_PATH = os.getenv('FOO_PATH')
MSG = os.getenv('MSG')

version = "v1.0.1"

if PORT is None:
    PORT = 3001

if FOO_PATH is None:
    FOO_PATH = "foo"

if MSG is None:
    MSG = "Hello foo"


@app.route(f'/{FOO_PATH}')
def hello_world():  # put application's code here
    return {
        "message": MSG,
        "version": version
    }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
