from flask import Blueprint, Flask, render_template, request, redirect, \
    url_for, jsonify

# Database model
from functools import wraps
from sqlalchemy import desc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Skills, Portfolio, Education, Work
from flask import session as login_session
from controllers import *
import random
import string


skills_blueprint = Blueprint('skill', __name__)
portfolio_blueprint = Blueprint('portfolio', __name__)
education_blueprint = Blueprint('education', __name__)
experience_blueprint = Blueprint('work', __name__)

engine = load_engine()
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Skills Routes


@skills_blueprint.route('/')
def skills():
    return render_template('list.html', skills=get_skills(), type='skills')


@skills_blueprint.route('/add', methods=['GET', 'POST'])
def add_skill():
    if request.method == 'POST':
        skills = get_skills()
        skill_type = Skills(skill=request.form['skill'],
                            level=request.form['level']
                            )
        session.add(skill_type)
        session.commit()
        return redirect(url_for('skill.skills'))
    else:
        return render_template('addSkill.html')


@skills_blueprint.route('/edit/<skill_id>', methods=['GET', 'POST'])
def edit_skill(skill_id):
    edit_skill = session.query(Skills).filter_by(id=skill_id).one()
    if request.method == 'POST':
        edit_skill.skill = request.form['skill']
        edit_skill.level = request.form['level']
        session.add(edit_skill)
        session.commit()
        return redirect(url_for('admin', skills=get_skills()))
    else:
        return render_template('editSkill.html', skill=edit_skill)


@skills_blueprint.route('/delete/<skill_id>', methods=['GET', 'POST'])
def delete_skill(skill_id):
    if request.method == 'POST':
        session.delete(get_skill(skill_id))
        session.commit()
        return redirect(url_for('admin'))
    else:
        return render_template('deleteSkill.html',
                               skill=get_skill(skill_id))

# Portfolio Routes


@portfolio_blueprint.route('/')
def portfolio():
    return render_template('list.html', portfolio=get_portfoilo(), type='portfolio')


@portfolio_blueprint.route('/add', methods=['GET', 'POST'])
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
                         created_month=request.form['created_month'],
                         created_year=request.form['created_year'],
                         service=request.form['service'],
                         image=request.form['image'])
        session.add(port)
        session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('modifyPortfolio.html', type='add')


@portfolio_blueprint.route('/edit/<portfolio_id>', methods=['GET', 'POST'])
def edit_portfolio(portfolio_id):
    port = session.query(Portfolio).filter_by(id=portfolio_id).one()
    if request.method == 'POST':
        port.title = request.form['title']
        port.skills_used = request.form['skills_used']
        port.demo_url = request.form['demo_url']
        port.github_url = request.form['github_url']
        port.description = request.form['description']
        port.client = request.form['client']
        port.created_month = request.form['created_month']
        port.created_year = request.form['created_year']
        port.service = request.form['service']
        port.image = request.form['image']
        session.add(port)
        session.commit()
        return redirect(url_for('portfolio.portfolio',
                                portfolio=get_portfoilo()))
    else:
        return render_template('modifyPortfolio.html', portfolio=port, type='edit')


@portfolio_blueprint.route('/delete/<portfolio_id>',
                           methods=['GET', 'POST'])
def delete_portfolio(portfolio_id):
    if request.method == 'POST':
        session.delete(get_portfolio(portfolio_id))
        session.commit()
        return redirect(url_for('admin'))
    else:
        return render_template('deletePortfilio.html',
                               portfolio=get_portfoilo())

# Education Routes


@education_blueprint.route('/')
def education():
    return render_template('list.html', education=get_education(), type='education')


@education_blueprint.route('/add', methods=['GET', 'POST'])
def add_education():
    if request.method == 'POST':
        education = get_education()
        school = Education(school=request.form['school'],
                           degree=request.form['degree'],
                           major=request.form['major'],
                           location=request.form['location'],
                           start_month=request.form['start_month'],
                           start_year=request.form['start_year'],
                           end_month=request.form['end_month'],
                           end_year=request.form['end_year'],
                           bullet_1=request.form['bullet_1'],
                           bullet_2=request.form['bullet_2'],
                           bullet_3=request.form['bullet_3']
                           )
        session.add(school)
        session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('modifyEducation.html', type='add')


@education_blueprint.route('/edit/<education_id>',
                           methods=['GET', 'POST'])
def edit_education(education_id):
    school = session.query(Education).filter_by(id=education_id).one()
    if request.method == 'POST':
        school.school = request.form['school']
        school.degree = request.form['degree']
        school.major = request.form['major']
        school.location = request.form['location']
        school.bullet_1 = request.form['bullet_1']
        school.bullet_2 = request.form['bullet_2']
        school.bullet_3 = request.form['bullet_3']
        school.start_month = request.form['start_month']
        school.start_year = request.form['start_year']
        school.end_month = request.form['end_month']
        school.end_year = request.form['end_year']

        session.add(school)
        session.commit()
        return redirect(url_for('education.education',
                                education=get_education()))
    else:
        return render_template('modifyEducation.html', education=school, type='edit')


@education_blueprint.route('/delete/<education_id>',
                           methods=['GET', 'POST'])
def delete_education(education_id):
    if request.method == 'POST':
        session.delete(get_education(education_id))
        session.commit()
        return redirect(url_for('admin'))
    else:
        return render_template('deleteEducation.html',
                               education=get_education())


# Experience Routes Routes


@experience_blueprint.route('/')
def experience():
    return render_template('list.html', experience=get_experience(), type='experience')


@experience_blueprint.route('/add', methods=['GET', 'POST'])
def add_experience():
    if request.method == 'POST':
        experience = get_experience()
        experience = Experience(experience=request.form['experience'],
                                degree=request.form['degree'],
                                major=request.form['major'],
                                location=request.form['location'],
                                description=request.form['description'],
                                start=request.form['start'],
                                end=request.form['end'])
        session.add(experience)
        session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('modifyExperience.html', type='add')


@experience_blueprint.route('/admin/experience/edit/<experience_id>',
                            methods=['GET', 'POST'])
def edit_experience(experience_id):
    experience = session.query(Work).filter_by(id=experience_id).one()
    if request.method == 'POST':
        experience.experience = request.form['experience'],
        experience.degree = request.form['degree'],
        experience.major = request.form['major'],
        experience.location = request.form['location'],
        experience.description = request.form['description'],
        experience.start = request.form['start'],
        experience.end = request.form['end']

        session.add(experience)
        session.commit()
        return redirect(url_for('experience.experience',
                                experience=get_experience()))
    else:
        return render_template('modifyExperience.html', experience=experience, type="edit")


@experience_blueprint.route('/admin/experience/delete/<experience_id>',
                            methods=['GET', 'POST'])
def delete_experience(experience_id):
    if request.method == 'POST':
        session.delete(get_experience(experience_id))
        session.commit()
        return redirect(url_for('admin'))
    else:
        return render_template('deleteexperience.html',
                               experience=get_experience())
