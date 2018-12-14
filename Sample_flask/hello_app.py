from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


# app decorator

@app.route('/', methods=['POST'])
def hello():
    message = request.get_json(force=True)
    name = message['name']
    
    response = dict(greeting='Hello,' + name + '!')

    return jsonify(response)
