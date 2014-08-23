import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
	name = "User1"
	links = ['Listings', 'Leases',
			'Pre-Construction', 
			'About Us', 'Contact']
	return render_template('index.html', name=name, links=links)

if __name__ == "__main__":
	app.run()
