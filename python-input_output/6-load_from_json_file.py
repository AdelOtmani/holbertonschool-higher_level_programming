#!/usr/bin/python3
"""Exercice 6 project Holberton Adel Otmani
"""

import json


def load_from_json_file(filename):
    """6. Create object from a JSON file

    Args:
        filename (_type_): name's file
        """
    with open(filename, 'r', encoding='utf-8') as Myfile:
        return (json.load(Myfile))
