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
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + ".json", 'w', encoding="utf8") as my_file:
            list = []
            if list_objs is not None:
                for o in list_objs:
                    list.append(o.to_dictionary())
            my_file.write(cls.to_json_string(list))
