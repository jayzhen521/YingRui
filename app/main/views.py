from flask import render_template, url_for, redirect
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home')
def home():
    return redirect(url_for('.index'))

@main.route('/services')
def services():
    return render_template('services.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/pricing')
def pricing():
    return render_template('pricing.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')
