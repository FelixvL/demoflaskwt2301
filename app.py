from flask import Flask
import felix
import omar
import jos

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/felix")
def ffelix():
    return felix.vanfelix()


@app.route("/omar")
def fomar():
    return omar.vanomar()

@app.route("/jos")
def fjos():
    return jos.vanjos()
