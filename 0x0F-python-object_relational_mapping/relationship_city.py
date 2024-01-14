#!/usr/bin/env python3
""" The imported mpdules """
from sqlalchemy import Column, Integer, String, text, ForeignKey
from relationship_state import Base


class City(Base):
    """ The class Defifnition """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
