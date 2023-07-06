#!/usr/bin/python3
"""Adds State object 'Louisiana' to the database"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to the MySQL server using command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create Session instance
    session = Session()

    # Create new State object
    new_state = State(name="Louisiana")

    # Add new_state to the session
    session.add(new_state)

    # Commit session to persist changes in the database
    session.commit()

    # Print new_state's id
    print(new_state.id)
