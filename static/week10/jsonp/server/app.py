import json

from flask import Flask 
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    text = open('test.json').read()
    return '{}({})'.format(request.args.get('callback', 'callback'), text)

if __name__ == '__main__':
    app.run(debug=True, port=5000)