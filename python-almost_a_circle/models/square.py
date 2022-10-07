#!/usr/bin/python3
"""square Class
    """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from class Rectangle

    Args:
        Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):

        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y}"
                f" - {self.size}")

    def update(self, *args, **kwargs):
        """adding the public methodthat assigns an argument to each attribute:
    1st argument should be the id attribute
    2nd argument should be the width attribute
    3rd argument should be the height attribute
    4th argument should be the x attribute
    5th argument should be the y attribute
        """
        a = 0
        if args:
            for arg in args:
                if a == 0:
                    self.id = arg
                if a == 1:
                    self.size = arg
                if a == 2:
                    self.x = arg
                if a == 3:
                    self.y = arg
                a += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

    def to_dictionary(self):
        """Square instance to dictionary representation

        Returns:
             that returns the dictionary representation of a square:


        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
