#!/usr/bin/python3
"""exo 3 project holberton"""


def inherits_from(obj, a_class):
    """ function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False."""
    return isinstance(type(obj), a_class) and not type(obj) is a_class

