from flask.ext.wtf import Form
from wtforms import TextField, BooleanField

class MailForm(Form)
	name = TextField('Name')
	email = TextField('Email')
	message = TextField('Message')