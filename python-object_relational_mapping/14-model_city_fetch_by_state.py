#!/usr/bin/python3
'''Module that list states in orm'''
from model_state import Base, State
from model_city import City
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

    cities = session.query(
                State.name, City.id, City.name
             ).join(
             City, City.state_id == State.id
             ).order_by(City.id.asc()).all()

    for city in cities:
        print(f'{city[0]}: ({city[1]}) {city[2]}')
