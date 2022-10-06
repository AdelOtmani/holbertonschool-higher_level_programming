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
