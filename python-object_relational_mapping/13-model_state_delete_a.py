#!/usr/bin/python3
"""Deletes all State objects with a name
containing the letter 'a' from the database"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to MySQL server using command-line arguments
    engine = create_engine('mysql+'
                           'mysqldb://{}:'
                           '{}@local'
                           'host/'
                           '{}'.format(sys.argv[1],
                                       sys.argv[2],
                                       sys.argv[3]), pool_pre_ping=True)

    # Create configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create Session instance
    session = Session()

    # Query State objects with names containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete State objects
    for state in states:
        session.delete(state)

    # Commit session to persist the changes in the database
    session.commit()
