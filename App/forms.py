from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import Required, Email

class MailForm(Form):
	nameid = StringField('Name', validators = [Required()])
	email = StringField('Email', validators = [Email()])
	message = TextAreaField('Message', validators = [Required()])