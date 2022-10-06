#!/usr/bin/python3
"""Rectangle Class
    """
from models.base import Base


class Rectangle(Base):
    """create class Rectangle that inherits from Base.
    Args:
        Base (class):
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area function

        Returns:
             the area value of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """display function
            that prints in stdout the Rectangle instance with the character #
        """
        c = "#"
        for new_line in range(self.y):
            print("")
        for i in range(self.height):
            for space in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print(c, end="")
            print("")

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}/{self.height}")

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
                    self.width = arg
                if a == 2:
                    self.height = arg
                if a == 3:
                    self.x = arg
                if a == 4:
                    self.y = arg
                a += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

    def to_dictionary(self):
        """_summary_

        Returns:
            that returns the dictionary representation of a Rectangle:
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
