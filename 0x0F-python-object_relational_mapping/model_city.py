#!/usr/bin/python3
"""script that lists all states from a database"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):

    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                unique=True,
                autoincrement="auto")
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
