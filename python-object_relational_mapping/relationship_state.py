#!/usr/bin/python3
"""
Defines a State model with a relationship to City.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """State class mapped to the states table."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Relationship with City; cascade deletes cities if state is deleted
    cities = relationship("City", backref="state", cascade="all, delete")