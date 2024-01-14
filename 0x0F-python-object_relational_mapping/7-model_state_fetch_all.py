#!/usr/bin/python3
""" The necessery imported modules """
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Sess = sessionmaker(bind=eng)
    sess = Sess()
    Base.metadata.create_all(eng)

    s_tate = sess.query(State).order_by(State.id).all()
    for state in s_tate:
        print("{}: {}".format(state.id, state.name))
    sess.close()
