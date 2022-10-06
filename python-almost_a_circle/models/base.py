#!/usr/bin/python3
"""Base class
    """


import json


class Base:
    """class initialisation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        """
        if list_dictionaries:
            return []
        return json.dumps(list_dictionaries)
