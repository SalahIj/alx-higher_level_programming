#!/usr/bin/python3
""" The imported modules """
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    db_user = argv[1]
    db_password = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(db_user, db_password, db_name),
                           pool_pre_ping=True)

    session = Session(engine)

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
