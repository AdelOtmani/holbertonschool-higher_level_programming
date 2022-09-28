#!/usr/bin/python3
"""Define a class   """


class MyInt(int):
    """ MyInt is a rebel. MyInt has == and != operators inverted

"""
    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
