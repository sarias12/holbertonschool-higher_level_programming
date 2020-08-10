#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_6_usa
"""
import sys
from model_city import Base, State, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sqlalchemy import asc, desc

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
            ),
        pool_pre_ping=True
        )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
