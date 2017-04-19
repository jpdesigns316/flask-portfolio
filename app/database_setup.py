# This is the creation of the database for the listing of the books as descirbed
# in the UDM.  This database is created using the tools for SQL Alchemy to create
# a database in sqlite.

# sqlalchemy imports needed to create the database.
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

engine = create_engine('sqlite:///' + os.path.join(BASE_DIR, 'website.db'))


Base = declarative_base()


class Skills(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    skill = Column(String, nullable=False)
    level = Column(Integer, nullable=False)

    def __init__(self, skill, level):
        self.skill = skill
        self.level = level


class Education(Base):
    __tablename__ = 'education'

    id = Column(Integer, primary_key=True)
    school = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    major = Column(String, nullable=False)
    location = Column(String, nullable=False)
    start = Column(String, nullable=False)
    end = Column(String, nullable=False)
    bullet_1 = Column(String)
    bullet_2 = Column(String)
    bullet_3 = Column(String)

    def __init__(self, school, degree, major,
                 location, start, end, bullet_1=None, bullet_2=None,
                 bullet_3=None,):
        self.school = school
        self.degree = degree
        self.major = major
        self.location = location
        self.start = start
        self.end = end
        self.bullet_1 = bullet_1
        self.bullet_2 = bullet_2
        self.bullet_3 = bullet_3


class Portfolio(Base):
    __tablename__ = 'portfolio'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    skills_used = Column(String, nullable=False)
    demo_url = Column(String, nullable=False)
    github_url = Column(String, nullable=False)
    description = Column(String)
    client = Column(String, nullable=False)
    created = Column(String, nullable=False)
    service = Column(String, nullable=False)
    image = Column(String, nullable=False)

    def __init__(self, title=None, skills_used=None, demo_url=None,
                 github_url=None,  description=None, client=None,
                 created=None, service=None,
                 image=None, modal_id=None):
        self.title = title
        self.skills_used = skills_used
        self.demo_url = demo_url
        self.github_url = github_url
        self.description = description
        self.client = client
        self.created = created
        self.service = service
        self.image = image

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'skills_used': self.skills_used,
            'demo_url': self.demo_url,
            'github_url': self.github_url,
            'description': self.description,
            'clent': self.client,
            'created': self.created,
            'service': self.service,
            'image': self.image
        }


class Work(Base):
    __tablename__ = 'work'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    start = Column(String)
    end = Column(String)
    location = Column(String)
    bullet_1 = Column(String)
    bullet_2 = Column(String)
    bullet_3 = Column(String)

    def __init__(self, title, company, start, end,
                 location, bullet_1=None, bullet_2=None, bullet_3=None):
        self.id = id
        self.title = title
        self.company = company
        self.location = location
        self.start = start
        self.end = end
        self.bullet_1 = bullet_1
        self.bullet_2 = bullet_2
        self.bullet_3 = bullet_3


class Settings(Base):
    __tablename__ = 'settings'

    id = Column(Integer, primary_key=True)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)

    def __init__(self, key, value):
        self.key = key
        self.value = value


Base.metadata.create_all(engine)
