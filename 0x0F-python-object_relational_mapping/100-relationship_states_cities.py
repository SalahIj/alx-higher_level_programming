#!/usr/bin/python3
""" The necessery imported modules """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.schema import Table

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2],
                                sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)

    sess = Session(eng)
    new_city = City(name='San Francisco')
    new = State(name='California')
    new.cities.append(new_city)
    sess.add_all([new, new_city])
    sess.commit()
    sess.close()
