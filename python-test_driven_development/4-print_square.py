#!/usr/bin/python3
"""say my name function"""


def print_square(size):
    """ print square of "#"
    """

    if type(size) != int or (type(size) == float and size == 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
