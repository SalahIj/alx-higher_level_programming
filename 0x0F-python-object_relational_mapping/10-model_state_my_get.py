#!/usr/bin/python3
""" The necessery imported modules """
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Sess = sessionmaker(bind=eng)

    sess = Sess()
    Base.metadata.create_all(eng)

    s_tate = sess.query(State).filter(State.name == argv[4]).first()

    if s_tate:
        print("{}".format(s_tate.id))
    else:
        print("Not found")
    sess.close()
