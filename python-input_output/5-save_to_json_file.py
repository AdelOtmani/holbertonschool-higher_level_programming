#!/usr/bin/python3
"""Exercice 5 project Holberton Adel Otmani
"""

import json


def save_to_json_file(my_obj, filename):
    """5. Save Object to a file

    Args:
        my_obj (_type_): object
        filename (_type_): name's file
        """
    with open(filename, 'a+', encoding='utf-8') as Myfile:
        return (json.dumps(Myfile))
