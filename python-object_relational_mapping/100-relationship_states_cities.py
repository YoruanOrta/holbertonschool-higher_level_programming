#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco” in the database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Database connection
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}")

    # Create tables in the database
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State and City
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # Add and commit changes
    session.add(new_state)
    session.add(new_city)
    session.commit()

    # Close session
    session.close()