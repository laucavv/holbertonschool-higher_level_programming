#!/usr/bin/python3
""" script 14-model_city_fetch_by_state.py that prints all City
    objects from the database hbtn_0e_14_usa
"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    ssesion = Session()
    result = ssesion.query(State, City).filter(State.id == City.state_id)
    for state_c, city_c in result:
        print("{}: ({}) {}".format(state_c.name, city_c.id, city_c.name))
    ssesion.close()
