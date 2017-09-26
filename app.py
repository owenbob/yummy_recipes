# app.py

# third party import
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "<html><h2>Welcome to Yummy Recipes V1.0</h2></html>"