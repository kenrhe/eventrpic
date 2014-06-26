from flask import Flask, render_template, request, session, redirect, jsonify
import jinja2
import os

import datetime
import pymongo
from pymongo import MongoClient

#making a new Flask app
app = Flask(__name__)

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
		return render_template('find.html')
	return redirect('/')

@app.route('/create', methods=['GET', 'POST'])
def create():
	if request.method == 'GET':
		return render_template('create.html')
	return redirect('/')


@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	#this code starts the web app, it can be found at http://localhost:8000
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port,debug=True)