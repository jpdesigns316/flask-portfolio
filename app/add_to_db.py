from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Education, Skills, Work, Portfolio

engine = create_engine('sqlite:///website.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Adding initial Admin for the generated books
school = Education(school="Udacity",
                   degree="Nanodegree",
                   major="Full Stack Web Design",
                   location="http://udacity.com",
                   start="June 2016",
                   end="Feburary 2016",
                   description="")
session.add(school)
session.commit()
