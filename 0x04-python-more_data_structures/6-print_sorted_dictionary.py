#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys"""
    for k in sorted(list(a_dictionary)):
        print("{}: {}".format(k, a_dictionary[k]))
