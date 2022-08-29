#!/usr/bin/python3
def no_c(my_string):
    m = ""
    for i in my_string:
        if i != "c" and i != "C":
            m += i
    return m
