#!/usr/bin/python3
""" function identation string"""


def text_indentation(text):
    """ function that prints a text with 2 new lines after
        each of these characters: ., ? and : """

    if type(text) != str:
        raise TypeError("text must be a string")
    check = False
    for i, letter in enumerate(text):
        if check and letter == " ":
            continue
        elif check and letter != " ":
            check = False
        if letter == "." or letter == "?" or letter == ":":
            print(letter)
            check = True
            print()
        else:
            print(letter, end="")
