from flask import Flask, render_template, request, url_for
import random
import json

app = Flask(__name__)

def r(items):
    return random.choice(items)

def g(what):
	return r(gacha[what])

limit = 20

gacha = ""
with open('gachabits.json', 'r') as file:
	gacha = json.load(file)

@app.route("/")
def home_route():
	return gacha

@app.route("/gacha/<what>/<int:num>")
def main_func(what, num):
	if what not in gacha.keys():
		return f"Gachabits does not contain a key named {what}"
	
	if num == 0:
		num = 1
	elif num > limit:
		num = limit
	
	final = []
	
	for i in range(num):
		current = g(what)
		final.append(current)
	return final