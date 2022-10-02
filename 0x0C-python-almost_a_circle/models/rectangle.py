#!/usr/bin/env python3
"""Rectangle class that inherits from base"""
from models.base import Base
class Rectangle(Base):
    """ Represents a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialise new rectangle class

            Args:
                width(int): private attribute
                height(int): private attribute
                x(int): private attribute
                y(int): private attribute
            Raises:
                TypeError: if width or height are not int
                ValueError: if width or height are less than 0
                TypeError: if x or y are not int
                ValueError: if x or y are less than 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """set or get the width of a triangle"""
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("width must be an int")
            if value <= 0:
                raise ValueError("width must be greater than zero")
            self.width = value

        @property
        def height(self):
            """set or get the width of a triangle"""
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("height must be an int")
            if value <= 0:
                raise ValueError("height must be greater than zero")
            self.height = value

        @property
        def x(self):
            """set or get the width of a triangle"""
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeError("x must be an int")
            if value <= 0:
                raise ValueError("x must be greater than zero")
            self.x = value
        @property
        def y(self):
            """set or get the width of a triangle"""
            return self.__y

        @y.setter
        def y(self, value):
            if type(value) != int:
                raise TypeError("y must be an int")
            if value <= 0:
                raise ValueError("y must be greater than zero")
            self.y = value
