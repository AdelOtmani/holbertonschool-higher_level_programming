#!/usr/bin/python3
"""Base class
    """


class Base:
    """class initialisation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
