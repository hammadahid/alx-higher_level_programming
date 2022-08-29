#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_lenght =  (-1) * (len(my_list))
    for i in range(-1,(list_lenght - 1), -1):
        print("{}".format(my_list[i]))
