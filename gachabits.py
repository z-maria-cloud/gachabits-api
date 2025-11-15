from flask import Flask, render_template, request, url_for
import random
import json

app = Flask(__name__)

# core functions

def r(items):
    return random.choice(items)

def g(what):
	return r(gacha[what])

# load core json file

gacha = ""
with open('gachabits.json', 'r') as file:
	gacha = json.load(file)

keys = sorted(list(gacha.keys()))
limit = 20

# list all the json file keys in the website's root

@app.route("/")
def gacha_home():
	return render_template("home.html", render_data={"gacha_keys": keys})

# main api function

@app.route("/gacha/<req_type>/<what>/<int:num>")
def gacha_main(what, num, req_type):
	
    # handle incorrect list names
	
	if what not in gacha.keys():
		return f"Gachabits does not contain a key named {what}"
	
    # handle results number

	if num == 0:
		num = 1
	elif num > limit:
		num = limit
	
	final = []
	
	for i in range(num):
		current = g(what)
		final.append(current)
	
    # choose wether to respond with raw data or with a web page

	if req_type == "api":
		return final
	elif req_type == "user":
		return render_template("detail.html", render_data={"results": final, "what": what, "num": num})

# list all entries from a given list name

@app.route("/test/<what>")
def gacha_test(what):
	return gacha[what]

@app.route("/word-count")
def gacha_stats():
	data = {}
	for i in keys:
		data[i] = len(gacha[i])
	return data