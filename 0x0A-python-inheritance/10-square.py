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


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that defines a Square from Rectangle class """
    def __init__(self, size):
        """ Method that initializes a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method that returns a string with the area """
        return super().area()
