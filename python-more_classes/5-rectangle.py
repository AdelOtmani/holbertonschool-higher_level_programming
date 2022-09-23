#!/usr/bin/python3
"""Define a class   """


class Rectangle:
    """Empty class

"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0:
            self.__width = 0

        if self.__width == 0:
            self.__height = 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        string = ""
        rec = "#"

        if self.__height == 0 or self.__width == 0:
            return ""

        for i in range(self.__height - 1):
            string += (rec * self.__width) + "\n"
        string += (rec * self.__width)
        return str(string)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
