from flask import Flask
import os
import sys


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello there!"

input () 
os.execl(sys.executable, sys.executable, *sys.argv)
