#!/usr/bin/python3
""" The necessery imported modules """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Sess = sessionmaker(bind=eng)

    sess = Sess()
    Base.metadata.create_all(eng)
    state_update = sess.query(State).filter_by(id='2').first()
    state_update.name = "New Mexico"

    sess.commit()
    sess.close()
