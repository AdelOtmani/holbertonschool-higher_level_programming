#!/usr/bin/python3
"""Define a class   """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Public instance method: def area(self):

"""
    def __init__(self, width, height):
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        print("[Rectangle] {}/{}".format(self.__width, self.__height))
        return (self.__width * self.__height)


r = Rectangle(3, 5)

print(r)
print(r.area())
