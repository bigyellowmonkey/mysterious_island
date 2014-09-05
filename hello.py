import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Contact' , methods = ['GET', 'POST'])
@app.route('/Contact.html' , methods = ['GET', 'POST'])
def contacts():
	
	return render_template('Contact.html')

	
if __name__ == "__main__":
	app.run()
 