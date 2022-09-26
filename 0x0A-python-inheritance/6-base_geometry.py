#!/usr/bin/python3
"""
   6-base_geometry.py module
   Class BaseGeometry, Public instance method: \
   def area(self): that raises an Exception with\
   the message area() is not implemented.
"""


class BaseGeometry:
    """ Empty class """
    def area(self):
        raise Exception("area() is not implemented")
