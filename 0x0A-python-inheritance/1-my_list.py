#!/usr/bin/python3
"""
   1-my_list module
   Class MyList that inherits from list that contain \
   Public instance method: def print_sorted(self): that \
   prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """ Class that inherits the attributes references of class list

    Args:
        list: class list

    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
