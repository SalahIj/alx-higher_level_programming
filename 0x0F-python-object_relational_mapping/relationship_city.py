#!/usr/bin/env python3
""" The necessery imported modules """
from sqlalchemy import Column, Integer, String, text, ForeignKey
from relationship_state import Base


class City(Base):
    """ The class definition """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
