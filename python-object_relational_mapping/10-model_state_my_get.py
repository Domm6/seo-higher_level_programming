#!/usr/bin/python3
"""Prints the State object with name from the database"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to MySQL server using command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create Session instance
    session = Session()

    # Get State object with given name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print result
    if state is None:
        print("Not found")
    else:
        print(state.id)
