#!/usr/bin/python3
"""Exercice 0 project Holberton Adel Otmani

  """


def read_file(filename=""):
    """functun read file
    Args:
        filename (str): ."".
    """

    with open(filename, encoding="utf-8") as Myfile:
        print(repr(Myfile))
