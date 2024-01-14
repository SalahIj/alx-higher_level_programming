#!/usr/bin/python3
""" The necessery imported modules """
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                         sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3])

    eng = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(eng)

    Sess = sessionmaker(bind=eng)
    sess = Sess()

    for a_city in sess.query(City).order_by(City.id):
        print("{}: {} -> {}".format(a_city.id, a_city.name,
                                    a_city.state.name))

    sess.close()
