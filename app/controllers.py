from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Skills, Portfolio, Education, Work, Certication, Config


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']
# Helper methods


def load_engine():
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    return engine


engine = load_engine()
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_education():
    return session.query(Education).all()


def get_school(education_id):
    return session.query(Education).filter_by(id=education_id).one()


def get_skills():
    return session.query(Skills).all()


def get_experience():
    return session.query(Work).all()


def get_skill(skills_id):
    return session.query(Skills).filter_by(id=skills_id).one()


def get_config():
    return session.query(Config).all()


def get_portfoilo():
    return session.query(Portfolio).all()


def get_project(portfolio_id):
    return session.query(Portfolio).filter_by(id=portfolio_id).one()


def config(meta_key):
    key = session.query(Config).filter_by(meta_key=meta_key).one()
    return key.meta_value


def clever_function(n):
    if n == 1:
        return 'January'
    elif n == 2:
        return 'February'
    elif n == 3:
        return 'March'
    elif n == 4:
        return 'April'
    elif n == 5:
        return 'May'
    elif n == 6:
        return 'June'
    elif n == 7:
        return 'July'
    elif n == 8:
        return 'August'
    elif n == 9:
        return 'September'
    elif n == 10:
        return 'October'
    elif n == 11:
        return 'November'
    elif n == 12:
        return 'December'
    else:
        return 'Present'
