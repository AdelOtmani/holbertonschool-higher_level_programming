#!/usr/bin/python3
"""exo 3 project holberton"""


def inherits_from(obj, a_class):
    """ function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False."""
    return isinstance(not type(obj), a_class)
