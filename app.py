from flask import Flask, render_template, request, session, redirect, jsonify
import jinja2
import os

import datetime
import pymongo
from pymongo import MongoClient

#making a new Flask app
app = Flask(__name__)

MONGO_URL = os.environ.get('MONGOHQ_URL')
client = MongoClient(MONGO_URL)
db = client.app26787337

events = db.events

#@app.route binds a function to specific url
@app.route('/')
#this function tells the app what to do when it loads the main page
def eventrpic():
	#render_template will render the index.html found in the template folder
	return render_template('index.html')

@app.route('/find', methods=['GET', 'POST'])
def find():
	#returning redirect will cause it do go to the specificed URL
	if request.method == 'GET':
		return render_template('find.html', events=events.find())
	return redirect('/')

@app.route('/loaderio-129dddcf59812b6327f243ede3b88349.txt', methods=['GET'])
def loadtest():
	return render_template('loaderio-129dddcf59812b6327f243ede3b88349.txt')

@app.route('/create', methods=['GET', 'POST'])
def create():
	if request.method == 'GET':
		return render_template('create.html')
	name=request.form['event-name']
	date=request.form['date']
	location=request.form['location']
	uid = name.replace(" ", "").lower()

	uid_scramble = 0
	while (events.find({"uid" : uid}).count() > 0):
		uid_scramble+=1
		uid = uid + str(uid_scramble)

	event = {"name" : name, "date" : date, "location" : location, "uid" : uid}
	event_id = events.insert(event)

	return render_template('create.html', error="Your event has been successfully created! The unique ID for this event is: " + uid)


@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	#this code starts the web app, it can be found at http://localhost:8000
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port,debug=True)