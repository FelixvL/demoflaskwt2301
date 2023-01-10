from flask import Flask
import felix

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/felix")
def ffelix():
    return felix.vanfelix()
