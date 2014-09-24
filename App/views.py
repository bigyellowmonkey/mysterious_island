from flask import render_template, flash, redirect, request
from app import app, mail
from forms import MailForm
from emails import send_email
from flask.ext.mail import Message
from config import ADMINS

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Contact' , methods = ['GET', 'POST'])
@app.route('/Contact.html' , methods = ['GET', 'POST'])
def contacts():
	form = MailForm()
	##form.nameid.data = form.validate_on_submit()
	if request.method == 'POST':
		msg = Message('yo wtf', sender = ADMINS[0], recipients = ADMINS)
		msg.body = 'wtf'
		msg.html = '<b>wtf</b>'
		mail.send(msg)
		
	
	return render_template('Contact.html'
		,form = form)

@app.route('/tmp.html' , methods = ['GET', 'POST'])
def tmp():
	##form = MailForm()
	return render_template('tmp.html'
		)


