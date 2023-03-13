#!/usr/bin/python3
'''Module that list states in orm'''
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1],
                            sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.execute(select([State.id, State.name]).where(State.id == 1))
    if not states:
        print("Nothing")
    else:
        for state in states:
            print('{}: {}'.format(state.id, state.name))

    session.close()
