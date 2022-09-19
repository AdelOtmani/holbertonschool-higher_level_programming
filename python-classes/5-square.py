#!/usr/bin/python3
"""Define a Square class   """


class Square(object):
    """private instance
"""

    def __init__(self, size=0):
        """init size"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """ check error"""

        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return current area"""

        return self.__size**2

    def my_print(self):
        """print # """
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
