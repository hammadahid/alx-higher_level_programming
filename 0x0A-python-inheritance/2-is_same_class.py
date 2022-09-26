#!/usr/bin/python3
"""
    2-is_same_class module
    Get if a object is exactly an instance of the \
    specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """ Function that returns True/False if obj is a type of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if type of obj is a_class
        False, otherwise
    """
    return type(obj) is a_class
