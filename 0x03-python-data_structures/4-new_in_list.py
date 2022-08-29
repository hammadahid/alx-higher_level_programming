#!/usr/bin/python3
def  new_in_list(my_list, idx, element):
    lenght_list = len(my_list)
    if idx < 0 and idx >= lenght_list:
        return my_list
    n_list = my_list[:]
    n_list[idx] = element
    return n_list
