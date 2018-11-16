# to run
# FLASK_APP=demo2.py flask run
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return("Hello World")


@app.route("/user/<usuario>")
def showUser(usuario):
        return("User: {}".format(usuario))
