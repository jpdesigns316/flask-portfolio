from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Books, User


def connect_to_db():
    engine = create_engine('sqlite:///books.db')
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session
