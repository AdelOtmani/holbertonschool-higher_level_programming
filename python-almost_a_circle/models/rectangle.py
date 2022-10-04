#!/usr/bin/python3
"""Rectangle Class
    """
from models.base import Base


class Rectangle(Base):
    """create class Rectangle that inherits from Base.
    Args:
        Base (class):
    """

    @property
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id=None)
