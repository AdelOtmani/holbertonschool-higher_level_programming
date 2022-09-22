#!/usr/bin/python3
"""say my name function"""


def say_my_name(first_name, last_name=""):
    """print first and last name"""

    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
