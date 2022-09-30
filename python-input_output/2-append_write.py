#!/usr/bin/python3
"""Exercice 2 project Holberton Adel Otmani

  """


def append_write(filename="", text=""):
    """writing append

    Args:
        filename (str): file's name.
        text (str): text write.

    Returns:
        _type_: _description_
    """

    with open(filename, 'a+', encoding='utf-8') as Myfile:
        Myfile.write(text)
    i = 0
    while i < len(text):
        i += 1
    return i
