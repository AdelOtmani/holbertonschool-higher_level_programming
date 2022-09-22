#!/usr/bin/python3
""" function identation string"""


def text_indentation(text):
    """ function that prints a text with 2 new lines after
        each of these characters: ., ? and : """

    if type(text) != str:
        raise TypeError("text must be a string")
    for letter in text:
        if letter == "." or letter == "?" or letter == ":":
            print(letter)
            print("")
        else:
            print(letter, end="")
