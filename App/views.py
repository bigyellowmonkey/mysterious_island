from flask import render_template, flash, redirect
from app import app
from forms import MailForm

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Contact' , methods = ['GET', 'POST'])
@app.route('/Contact.html' , methods = ['GET', 'POST'])
def contacts():
	##form = MailForm()
	return render_template('Contact.html'
		)

@app.route('/Contact.html' , methods = ['GET', 'POST'])
def map():
	
	return render_template('map.html')
