#!/usr/bin/python3
""" Fetch database stuff """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == '__main__':
    """ create the 'engine' """

    """ I know this is ugly. I had to use pep8 which limits line chars """
    eng_log = "{}:{}".format(sys.argv[1], sys.argv[2])
    eng_s = '://{}@localhost/{}'.format(eng_log, sys.argv[3])
    engine = create_engine('mysql+mysqldb{}'.format(eng_s), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    """ Create a session, i had to bind the engine differently """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Print out our query :) """
    print(session.query(State).order_by(State.id).first().id, end=": ")
    print(session.query(State).order_by(State.id).first().name)

    """ Close the session """
    session.close()
