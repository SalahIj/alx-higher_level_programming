#!/usr/bin/env python3
""" the necessery imported modules """
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(argv[1], argv[2],
                                argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(eng)
    Sess = sessionmaker(bind=eng)
    sess = Sess()

    new_state = State(name="California")
    sess.add(new_state)
    sess.commit()
    new_city = City(name="San Francisco", state_id=new_state.id)
    sess.add(new_city)
    sess.commit()
    sess.close()
