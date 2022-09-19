#!/usr/bin/python3
"""Define a Square class   """


class Square(object):
    """private instance
"""

    def size(self, size=0):
        """init size"""
        self.__size = size

    def size(self):
        return self.__size

    def __init__(self, value):
        """ check error"""

        if (type(value) != int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return current area"""

        return self.__size**2
