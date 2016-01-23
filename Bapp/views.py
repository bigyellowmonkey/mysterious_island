from flask import render_template, flash, redirect, request
from app import app, mail
from forms import MailForm
from emails import send_email
from flask.ext.mail import Message
from config import ADMINS, EMAIL_LANDER

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Contact' , methods = ['GET', 'POST'])
@app.route('/Contact.html' , methods = ['GET', 'POST'])
def contacts():
	form = MailForm()
	#form.nameid.data = form.validate_on_submit()
	
	print form.validate()
	print form.errors
	
	if request.method == 'POST' and form.validate():
		#form.nameid.data = 'vlad!'
		msg = Message('New Inquiry from ' + form.nameid.data, sender = ADMINS[0], recipients = EMAIL_LANDER)
		msg.body = form.email.data
		msg.html = '<b>'+form.email.data+'</b> </br>' + form.message.data
		mail.send(msg)
		
	
	return render_template('Contact.html'
		,form = form)

@app.route('/tmp.html' , methods = ['GET', 'POST'])
def tmp():
	#form = MailForm()
	return render_template('tmp.html'
		)


