#!/usr/bin/python3
""" that contains the class definition of a City. """


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """Class """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement="auto",
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
