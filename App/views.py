from flask import render_template, flash, redirect
from app import app
from forms import MailForm

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Contact' , methods = ['GET', 'POST'])
@app.route('/Contact.html' , methods = ['GET', 'POST'])
def contacts():
	form = MailForm()
	##form.nameid.data = form.validate_on_submit()
	if request.method == 'POST':
		form.nameid.data = 'POST'
		form.email.data = 'someshit'
	
	return render_template('Contact.html'
		,form = form)

@app.route('/tmp.html' , methods = ['GET', 'POST'])
def tmp():
	##form = MailForm()
	return render_template('tmp.html'
		)


