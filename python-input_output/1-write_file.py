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
        for i, c in enumerate.text:
            pass
        return c
        print(Myfile.read(), end="")
