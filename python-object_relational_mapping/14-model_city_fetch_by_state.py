#!/usr/bin/python3
"""Prints all City objects from the database"""


import sys
from model_state import Base, State
from model_city import City
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

    # Query City objects and sort by id
    cities = session.query(City).order_by(City.id).all()

    # Print cities by state
    for city in cities:
        state = session.query(State).filter(State.id == city.state_id).first()
        print("{}: ({}) {}".format(state.name, city.id, city.name))
