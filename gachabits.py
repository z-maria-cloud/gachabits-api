from flask import Flask, render_template, request, url_for
from random import randint
import json

app = Flask(__name__)

gacha = ""
with open('gachabits.json', 'r') as file:
	gacha = json.load(file)

@app.route("/")
def home_route():
	return gacha