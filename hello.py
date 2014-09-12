import os
from flask import Flask
from flask import render_template
from flask.ext.mail import Message
from app import app, mail
from Config import ADMINS

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Contact' , methods = ['GET', 'POST'])
@app.route('/Contact.html' , methods = ['GET', 'POST'])
def contacts():
	
	return render_template('Contact.html')

@app.route('/Contact.html' , methods = ['GET', 'POST'])
def map():
	
	return render_template('map.html')

	
	
if __name__ == "__main__":
	app.run()
 