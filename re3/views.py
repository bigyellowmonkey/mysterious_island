from flask import render_template, flash, redirect, request
from re3 import app

@app.route('/')
def start():
	return render_template('index.html')


@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/brokerage_service.html')
def brokerage_service():
	return render_template('brokerage_service.html')

@app.route('/property_management.html')
def property_management():
	return render_template('property_management.html')

@app.route('/interior_design.html')
def interior_design():
	return render_template('interior_design.html')


@app.route('/investment.html')
def investment():
	return render_template('investment.html')

@app.route('/commercial_connect.html')
def commercial_connectinvestment():
	return render_template('commercial_connect.html')





def _404():
	return render_template('404.html')

@app.route('/about.html')
def about():
	return render_template('about.html')


@app.route('/blog-home-1.html')
def blog_home_1():
	return render_template('blog-home-1.html')


@app.route('/blog-home-2.html')
def blog_home_2():
	return render_template('blog-home-2.html')


@app.route('/blog-post.html')
def blog_home_post():
	return render_template('blog-post.html')


@app.route('/contact.html')
def contact():
	return render_template('contact.html')


@app.route('/faq.html')
def faq():
	return render_template('faq.html')


@app.route('/full-width.html')
def full_width_html():
	return render_template('full-width.html')


@app.route('/portfolio-1-col.html')
def portfolio_1():
	return render_template('portfolio-1-col.html')


@app.route('/portfolio-2-col.html')
def portfolio_2():
	return render_template('portfolio-2-col.html')

@app.route('/portfolio-3-col.html')
def portfolio_3():
	return render_template('portfolio-3-col.html')


@app.route('/portfolio-4-col.html')
def portfolio_4():
	return render_template('portfolio-4-col.html')

@app.route('/portfolio-item.html')
def portfolio_item():
	return render_template('portfolio-item.html')

@app.route('/pricing.html')
def pricing():
	return render_template('pricing.html')

@app.route('/services.html')
def services():
	return render_template('services.html')

@app.route('/sidebar.html')
def sidebar():
	return render_template('sidebar.html')


