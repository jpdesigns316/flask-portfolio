from flask import Blueprint, Flask, render_template, request, redirect, \
    url_for, jsonify

# Database model
from functools import wraps
from sqlalchemy import desc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Skills
from flask import session as login_session
from controllers import load_engine, get_education, get_school, get_skills,  \
    get_skill, get_portfoilo, get_project, get_experience
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
    return render_template('skills.html', skills=get_skills())


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
    return render_template('portfolio.html', portfolio=get_portfoilo())


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
                         created=request.form['created'],
                         service=request.form['service'],
                         image=request.form['image'])
        session.add(port)
        session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('addPortfolio.html')


# Education Routes
@education_blueprint.route('/')
def education():
    return render_template('education.html', education=get_education())


@education_blueprint.route('/add', methods=['GET', 'POST'])
def add_education():
    if request.method == 'POST':
        education = get_education()
        school = Education(school=request.form['school'],
                           degree=request.form['degree'],
                           major=request.form['major'],
                           location=request.form['location'],
                           bullet_1=request.form['bullet_1'],
                           bullet_2=request.form['bullet_2'],
                           bullet_3=request.form['bullet_3'],
                           start=request.form['start'],
                           end=request.form['end'])
        session.add(school)
        session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('addEducation.html')


@education_blueprint.route('/edit/<education_id>',
                           methods=['GET', 'POST'])
def edit_education(education_id):
    school = session.query(Education).filter_by(id=education_id).one()
    if request.method == 'POST':
        school.school = request.form['school'],
        school.degree = request.form['degree'],
        school.major = request.form['major'],
        school.location = request.form['location'],
        school.bullet_1 = request.form['bullet_1'],
        school.bullet_2 = request.form['bullet_2'],
        school.bullet_3 = request.form['bullet_3'],
        school.start = request.form['start'],
        school.end = request.form['end']

        session.add(school)
        session.commit()
        return redirect(url_for('education.education',
                                education=get_education()))
    else:
        return render_template('editEducation.html', education=school)


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


# Experience Routes# Routes


@experience_blueprint.route('/')
def experience():
    return render_template('experience.html', experience=get_experience())


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
        return render_template('addexperience.html')


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
        return render_template('editexperience.html', experience=experience)


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
