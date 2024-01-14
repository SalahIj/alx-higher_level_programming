#!/usr/bin/python3
""" The imported necessery modules """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """Class definition"""
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City",
                          cascade="all, delete-orphan",
                          backref=backref("state", cascade="all"),
                          single_parent=True)
