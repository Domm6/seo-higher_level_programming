#!/usr/bin/python3
"""Changes name of State object in database"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to MySQL server using command-line arguments
    engine = create_engine('mysql'
                           '+mysqldb:'
                           '//{}:{}@localhost/'
                           '{}'.format(sys.argv[1],
                                       sys.argv[2],
                                       sys.argv[3]), pool_pre_ping=True)

    # Create configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create Session instance
    session = Session()

    # Query State object with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Update name of the State to "New Mexico"
    state.name = "New Mexico"

    # Commit session to persist the changes in the database
    session.commit()
