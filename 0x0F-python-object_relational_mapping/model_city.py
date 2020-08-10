#!/usr/bin/python3
"""contains the class definition of a City and an instance Base
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model_state import State, Base


class City(Base):
    """Class for cities table  with  id and name colum.

    Args:
        Base: [Inherits from Base]
    """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        autoincrement=True,
        primary_key=True,
        nullable=False
        )
    name = Column(
        String(128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey('states.id')
    )
    parent = relationship("State", back_populates="child")
