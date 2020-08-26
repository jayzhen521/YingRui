import logging
from flask import render_template, url_for, redirect, current_app
from .forms import ContactMsg
from . import main
from ..email import send_email
from ..models import Contactor

def send_contact_email(app, form):
    username = form.username.data
    email = form.email.data
    phonenumber = form.phonenumber.data
    message = form.message.data

    contactor = Contactor(username, email, phonenumber, message)
    send_email(app.config['CONTACT_RECEIVER'], 'Contactor', 'mail/contactor', contactor=contactor)

@main.route('/', methods=['GET', 'POST'])
def index():
    app = current_app._get_current_object()
    form = ContactMsg()
    if form.validate_on_submit():
        #send email to joyousContect@outlook.com
        if form.validate_on_submit():
            send_contact_email(app, form)
    return render_template('index.html', form=form)

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

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    app = current_app._get_current_object()
    form = ContactMsg()
    if form.validate_on_submit():
        send_contact_email(app, form)
        return redirect(url_for('.index'))
    return render_template('contact.html', form=form)



