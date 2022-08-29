#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lenght_array = len(my_list)
    if idx <= lenght_array and idx != 0:
        my_list[idx] = element
    return my_list
