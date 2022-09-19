#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print c elements of a list"""
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
            print()
    except IndexError:
        print()
        return i
    else:
        return x
