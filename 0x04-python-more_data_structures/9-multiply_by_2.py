#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multipled by 2"""
    a = {}
    for i in a_dictionary:
        a[i] = (a_dictionary[i] * 2)
    return a
