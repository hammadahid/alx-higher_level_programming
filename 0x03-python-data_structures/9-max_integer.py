#!/usr/bin/python3
def max_integer(my_list=[]):
    """finds the biggerst integer of a list"""
    if len(my_list) == 0:
        return None
    maxNum = my_list[0]
    for i in my_list:
        if i > maxNum:
            maxNum = i
    return maxNum
