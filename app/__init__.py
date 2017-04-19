
from flask import Flask, render_template, request, make_response, redirect, url_for, session, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Skills, Education, Portfolio, Work

from functools import wraps

import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import requests
from flask import session as login_session


from views.skills import skills_blueprint
from education.skills import education_blueprint
from views.skills import skills_blueprint
from views.education import education_blueprint

# Register Flask Blueprints
app.register_blueprint(skills_blueprint, url_prefix='/admin/skills')
app.register_blueprint(education_blueprint, url_prefix='/admin/education')
app.register_blueprint(skills_blueprint, url_prefix='/admin/portfolio')
app.register_blueprint(experience_blueprint, url_prefix='/admin/experience')

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']


engine = create_engine('sqlite:///website.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def home():
    return render_template('index.html',
                           title="JP Designs",
                           education=get_education(),
                           skills=get_skills(),
                           portfolio=get_portfoilo())


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
        return render_template('admin.html')
    else:
        return redirect(url_for('login'))


@app.route('/admin/skill')
def skills():
    return render_template('skills.html', title="JP Designs", skills=get_skills())


@app.route('/admin/portfolio')
def portfolio():
    return render_template('portfolio.html', title="JP Designs", portfolio=get_portfoilo())


@app.route('/admin/educaiton')
def education():
    return render_template('education.html', title="JP Designs", education=get_education())


@app.route('/admin/skill/add', methods=['GET', 'POST'])
def add_skill():
    if request.method == 'POST':
        skills = get_skills()
        # Creating a books object to add to the databse.
        skill_type = Skills(skill=request.form['skill'],
                            level=request.form['level']
                            )
        session.add(skill_type)
        session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('addSkill.html')


@app.route('/admin/skill/edit/<skill_id>', methods=['GET', 'POST'])
def edit_skill(skill_id):
    edit_skill = session.query(Skills).filter_by(id=skill_id).one()
    if request.method == 'POST':
        edit_skill.skill = request.form['skill']
        edit_skill.level = request.form['level']
        session.add(edit_skill)
        session.commit()
        return redirect(url_for('skills'))
    else:
        return render_template('editSkill.html', skill=edit_skill)


@app.route('/admin/skill/delete/<skill_id>', methods=['GET', 'POST'])
def delete_skill(skill_id):
    if request.method == 'POST':
        session.delete(get_skill(skill_id))
        session.commit()
        return redirect(url_for('admin'))
    else:
        return render_template('deleteSkill.html',
                               skill=get_skill(skill_id))


@app.route('/admin/portfolio/add', methods=['GET', 'POST'])
def add_portfolio():
    if request.method == 'POST':
        portfolio = session.query(Portfolio).all()
        # Creating a books object to add to the databse.
        port = Portfolio(title=request.form['title'],
                         skills_used=request.form['skills_used'],
                         demo_url=request.form['demo_url'],
                         github_url=request.form['github_url'],
                         description=request.form['description'],
                         client=request.form['client'],
                         created=request.form['created'],
                         service=request.form['service'],
                         image=request.form['image'])
        session.add(port)
        session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('addPortfolio.html')


@app.route('/admin/education/add', methods=['GET', 'POST'])
def add_education():
    if request.method == 'POST':
        education = get_education()
        # Creating a books object to add to the databse.
        school = Educaiton(school=request.form['school'],
                           degree=request.form['degree'],
                           major=request.form['major'],
                           location=request.form['location'],
                           description=request.form['description'],
                           start=request.form['start'],
                           end=request.form['end'])
        session.add(school)
        session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('addEducation.html')


@app.route('/admin/education/edit/<education_id>')
def edit_education(education_id):
    pass


@app.route('/admin/education/delete/<education_id>')
def delete_education(education_id):
    pass


def get_education():
    return session.query(Education).all()


def get_skills():
    return session.query(Skills).all()


def get_skill(skill_id):
    return session.query(Skills).filter_by(id=skill_id).one()


def get_portfoilo():
    return session.query(Portfolio).all()
