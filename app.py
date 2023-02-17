from flask import Flask

app = Flask(__name__)


@app.route('/foo')
def hello_world():  # put application's code here
    return 'Hello foo'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
