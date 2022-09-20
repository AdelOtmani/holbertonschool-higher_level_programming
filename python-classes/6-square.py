#!/usr/bin/python3
"""Define a Square class   """


class Square(object):
    """private instance
"""

    def __init__(self, size=0, position=(0, 0)):
        """init size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        """ check error"""

        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if (len(value) != 2 or
                not all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """return current area"""

        return self._size * self._size

    def my_print(self):
        """print # """
        if self._size > 0:
            for n in range(self._position[1]):
                print("")
            for i in range(self._size):
                for m in range(self._position[0]):
                    print("", end="")
                for j in range(self._size):
                    print("#", end="")
                print("")
        else:
            print("")
