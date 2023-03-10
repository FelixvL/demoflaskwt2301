from flask import Flask
import felix
import omar
import jos
import just
import floris

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/felix")
def ffelix():
    return felix.vanfelix()

@app.route("/zoekpokemon/<naampokemon>")
def ffelix2(naampokemon):
    return felix.zoekpokemon(naampokemon)

@app.route("/omar")
def fomar():
    return omar.vanomar()

@app.route("/jos")
def fjos():
    return jos.vanjos()

@app.route("/just")
def fjust():
    return just.vanjust()

@app.route("/floris")
def ffloris():
    return floris.vanfloris()
