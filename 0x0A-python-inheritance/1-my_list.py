#!/usr/bin/python3
"""
Inheritance class
"""

class MyList(list):
    """
    priints the list but
    sorted
    Args:
    self: the object
    """
    def print_sorted(self):
        new_list = []
        for i in self:
            new_list.append(i)
        print(sorted(new_list))
        