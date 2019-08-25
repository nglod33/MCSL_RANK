# Author: Nate Glod
# File: Main.py
# Defines behavior for the MCSL_RANK web app

import flask as fl
app = fl.Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return '<h1>Home Page</h1>'


@app.route('/about')
def about():
    return '<h1>About</h1>'


