# to run
# FLASK_APP=demo1.py flask run
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return("Hello World")
