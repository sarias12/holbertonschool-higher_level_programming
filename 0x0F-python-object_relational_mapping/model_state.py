#!/usr/bin/python3
"""contains the class definition of a State and an instance Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class for states table  with  id and name colum.

    Args:
        Base: [Inherits from Base]
    """
    __tablename__ = 'states'
    id = Column(
        'id',
        Integer,
        autoincrement=True,
        primary_key=True,
        nullable=False
        )
    name = Column(
        String(128),
        nullable=False
    )
