from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/getData")
def hello():
    return "Hello Someone!"












