#!/usr/bin/python3
"""advanced ex 101 project 2 Holberton Adel Otmani"""


def add_attribute(obj, att, value):
    """function that adds a new attribute to an object if it’s possible """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
