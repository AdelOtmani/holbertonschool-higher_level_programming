#!/usr/bin/python3
"""Define a Square class   """


class Square(object):
    """private instance
"""

    def __init__(self, size=0):
        """init size"""
        self.__size = size
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """return current area"""

        return self._size * self.__size
