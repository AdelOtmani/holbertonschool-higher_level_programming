#!/usr/bin/python3
""" class inherits"""


class MyList(list):
    """ class MyList that inherits from list"""

    def __init__(self):
        self = []

    def print_sorted(self):
        print(sorted(self))
