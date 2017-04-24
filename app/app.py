from flask import Flask, render_template, request, make_response, redirect, \
    url_for, session, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Skills, Education, Portfolio, Work
from controllers import *
from functools import wraps

import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import requests
from flask import session as login_session
from config import user_configuration

from views import skills_blueprint, education_blueprint, portfolio_blueprint, \
    experience_blueprint


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']

# Register Flask Blueprints
app.register_blueprint(skills_blueprint, url_prefix='/admin/skills')
app.register_blueprint(education_blueprint, url_prefix='/admin/education')
app.register_blueprint(portfolio_blueprint, url_prefix='/admin/portfolio')
app.register_blueprint(experience_blueprint, url_prefix='/admin/experience')

app.jinja_env.globals.update(clever_function=clever_function)

app.jinja_env.globals.update(number_to_string=number_to_string)


engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def home():
    return render_template('index.html',
                           title="JP Designs",
                           education=get_education(),
                           skills=get_skills(),
                           portfolio=get_portfoilo(),
                           experience=get_experience(),
                           data=get_data())


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if (request.form['username'] != 'admin') \
                or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            login_session['username'] = 'Admin'
            flash('You were logged in.')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    login_session.clear()
    return redirect(url_for('home'))


@app.route('/admin')
def admin():
    if 'username' in login_session:
        return render_template('admin.html', test=user_configuration())
    else:
        return redirect(url_for('login'))
