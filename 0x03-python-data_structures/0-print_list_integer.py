#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """prints all integers of a list"""
    lenght_list = len(my_list)
    for i in range(0, lenght_list):
        print("{:d}".format(my_list[i]));
