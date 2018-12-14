from flask import Flask

app = Flask(__name__)  # creats instance of flask class: single module


@app.route('/')
def running():
    return "Flask is running"
