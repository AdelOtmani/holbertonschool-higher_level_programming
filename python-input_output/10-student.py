#!/usr/bin/python3
"""Exercice 10 project holberton Adel Otmani
"""


class Student:
    """class student
        Public instance attributes:
                first_name
                last_name
                age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) == list and
                all((type(i)) == str for i in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
