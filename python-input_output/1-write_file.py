#!/usr/bin/python3
"""Exercice 1 project Holberton Adel Otmani

  """


def write_file(filename="", text=""):
    """ funct write file

    Args:
        filename (str): file's name.
        text (str): text write.
    """

    with open(filename, 'w', encoding='utf-8') as Myfile:
        Myfile.write(text)
    i = 0
    while i < len(text):
        i+=1
    return i
