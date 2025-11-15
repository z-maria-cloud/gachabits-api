from flask import Flask, render_template, request, url_for
from random import randint

app = Flask(__name__)

@app.route("/")
def home_route():
	return "<p>Hello, World!</p>"