#!/usr/bin/python3
""" The necessery imported modules """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Sess = sessionmaker()
    sess = Sess(bind=eng)

    Base.metadata.create_all(eng)
    s_tate = sess.query(State).order_by(State.id).first()

    if s_tate:
        print("{}: {}".format(s_tate.id, s_tate.name))
    else:
        print("Nothing")
    sess.close()
