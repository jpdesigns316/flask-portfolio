from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Skills(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    skill = Column(String, nullable=False)
    level = Column(Integer, nullable=False)

    def __init__(self, skill, level):
        self.skill = skill
        self.level = level

    def serialize(self):
        return {
            'id': self.id,
            'skill': self.skill,
            'level': self.level
        }


class Education(Base):
    __tablename__ = 'education'

    id = Column(Integer, primary_key=True)
    school = Column(String)
    degree = Column(String)
    major = Column(String)
    location = Column(String)
    start_month = Column(String)
    start_year = Column(Integer)
    end_month = Column(String)
    end_year = Column(Integer)
    bullet_1 = Column(String)
    bullet_2 = Column(String)
    bullet_3 = Column(String)

    def __init__(self, school, degree, major, location, start_month,
                 start_year, end_month, end_year, bullet_1=None,
                 bullet_2=None, bullet_3=None,):
        self.school = school
        self.degree = degree
        self.major = major
        self.location = location
        self.start_mo = start_month
        self.start_year = start_year
        self.end_month = end_month
        self.end_year = end_year
        self.bullet_1 = bullet_1
        self.bullet_2 = bullet_2
        self.bullet_3 = bullet_3

    def serialize(self):
        return {
            'id': self.id,
            'school': self.school,
            'degree': self.degree,
            'major': self.major,
            'locaiton': self.locaiton,
            'start_month': self.start_month,
            'start_year': self.start_year,
            'end_month': self.end_month,
            'end_year': self.end_year,
            'bullet_1': self.bullet_1,
            'bullet_2': self.bulet_2,
            'bullet_3': self.bullet_3
        }


class Portfolio(Base):
    __tablename__ = 'portfolio'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    skills_used = Column(String, nullable=False)
    demo_url = Column(String, nullable=False)
    github_url = Column(String, nullable=False)
    description = Column(String)
    client = Column(String, nullable=False)
    created_month = Column(String, nullable=False)
    created_year = Column(Integer, nullable=False)
    service = Column(String, nullable=False)
    image = Column(String, nullable=False)

    def __init__(self, title=None, skills_used=None, demo_url=None,
                 github_url=None,  description=None, client=None,
                 created_month=None, created_year=None, service=None,
                 image=None):
        self.title = title
        self.skills_used = skills_used
        self.demo_url = demo_url
        self.github_url = github_url
        self.description = description
        self.client = client
        self.created_month = created_month
        self.created_year = created_year
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
            'created_month': self.created_month,
            'created_year': self.created_year,
            'service': self.service,
            'image': self.image
        }


class Work(Base):
    __tablename__ = 'work'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    start_month = Column(String, nullable=False)
    start_year = Column(Integer, nullable=False)
    end_month = Column(String, nullable=False)
    end_year = Column(Integer)
    location = Column(String)
    bullet_1 = Column(String)
    bullet_2 = Column(String)
    bullet_3 = Column(String)

    def __init__(self, title, company, start_month, start_year, end_month,
                 end_year, location, bullet_1=None, bullet_2=None,
                 bullet_3=None):
        self.id = id
        self.title = title
        self.company = company
        self.location = location
        self.start_month = start_month
        self.start_year = start_year
        self.end_month = end_month
        self.end_year = end_year
        self.bullet_1 = bullet_1
        self.bullet_2 = bullet_2
        self.bullet_3 = bullet_3

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'start_month': self.start_month,
            'start_year': self.start_year,
            'end_month': self.end_month,
            'end_year': self.end_year,
            'bullet_1': self.bullet_1,
            'bullet_2': self.bulet_2,
            'bullet_3': self.bullet_3
        }


class Certication(Base):
    __tablename__ = 'certifiation'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    authority = Column(String, nullable=False)
    license_no = Column(String)
    from_month = Column(Integer, nullable=False)
    from_year = Column(Integer, nullable=False)
    to_month = Column(String)
    to_year = Column(Integer)
    certification_url = Column(String)

    def __init__(self, name, authority, license_no, from_month, form_year,
                 to_month, to_year, certification_url):
        self.id = id
        self.name = name
        self.authority = authority
        self.license_no = license_no
        self.from_month = from_month
        self.from_year = from_year
        self.to_month = to_month
        self.to_year = to_year
        self.certification_url = certification_url


engine = create_engine('sqlite:///website.db')


Base.metadata.create_all(engine)
