#!/usr/bin/python3
"""Define a Square class   """


class Square(object):
    """private instance
"""

    def __init__(self, size=0, position=(0, 0)):
        """init size"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self, value):
        if value != 2 or type(value) != int:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def area(self):
        """return current area"""

        return self.__size**2

    def my_print(self):
        """print # """
        if self.__size > 0:
            for n in range(self.__position[1]):
                print("$")
            for i in range(self.__size):
                for m in range(self.__position[0]):
                    print("$", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")

    def position(self):
        return self.__position
