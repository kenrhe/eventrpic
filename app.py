from flask import Flask, render_template, request, session, redirect, jsonify
import jinja2
import os

#making a new Flask app
app = Flask(__name__)

#@app.route binds a function to specific url
@app.route('/')
#this function tells the app what to do when it loads the main page
def eventrpic():
	#render_template will render the index.html found in the template folder
	return 'hello world'

if __name__ == '__main__':
	#this code starts the web app, it can be found at http://localhost:8000
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port,debug=True)