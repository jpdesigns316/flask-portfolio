from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Skills, Portfolio, Education, Work


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
    return session.query(Skill).filter_by(id=skills_id).one()


def get_portfoilo():
    return session.query(Portfolio).all()


def get_project(portfolio_id):
    return session.query(Portfolio).filter_by(id=portfolio_id).one()
