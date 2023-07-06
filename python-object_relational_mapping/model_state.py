#!/usr/bin/python3
"""Start link class to table in database"""


import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

# Create instance of Base as the base class for class definitions
Base = declarative_base()


class State(Base):
    """State class representing a state entity in the MySQL table 'states'."""

    # Table name in the database
    __tablename__ = 'states'

    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"<State(id={self.id}, name='{self.name}')>"


if __name__ == "__main__":
    # Connect to the MySQL server using command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the table(s) based on the class definitions
    Base.metadata.create_all(engine)
