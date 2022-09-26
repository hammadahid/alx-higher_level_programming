#!/usr/bin/python3
"""
   6-base_geometry.py module
   Class BaseGeometry.
   Public instance method: \
   def area(self): that raises an Exception with\
   the message area() is not implemented.
   Public instance method:\
   def integer_validator(self, name, value):\
   that validates value
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that defines a rectangle from BaseGeometry Class """

    def __init__(self, width, height):
        """ Initializes instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
