#!/usr/bin/python3
"""Rectangle Class
    """
from turtle import heading, width
from models.base import Base


class Rectangle(Base):
    """create class Rectangle that inherits from Base.
    Args:
        Base (class):
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(self.__width))
        if value <= 0:
            raise ValueError(f"{self.__width} must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(self.__height))
        if value <= 0:
            raise ValueError(f"{self.__height} must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value <= 0:
            raise ValueError(f"{self.__x} must be > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value <= 0:
            raise ValueError(f"{self.__y} must be > 0")
        self.__y = value
