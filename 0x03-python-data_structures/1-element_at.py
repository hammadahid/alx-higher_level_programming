#!/usr/bin/python3
def element_at(my_list, idx):
    lenght_array = len(my_list)
    if idx < 0 or idx >= lenght_array:
        return None
    return my_list[idx]
