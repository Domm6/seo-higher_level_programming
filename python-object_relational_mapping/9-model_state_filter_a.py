#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to MySQL server using command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create Session instance
    session = Session()

    # Query State objects that have the letter 'a' and order by id
    states = session.query(State).filter(State.name.
                                         like('%a%')).order_by(State.id).all()

    # Print results
    for state in states:
        print("{}: {}".format(state.id, state.name))
