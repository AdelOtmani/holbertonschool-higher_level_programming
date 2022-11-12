#!/usr/bin/python3
"""
Class State, that contains the class definition of a State and an instance
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """
    inherits from Base
    """
    __table_name__ = "states"
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
