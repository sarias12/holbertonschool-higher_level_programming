#!/usr/bin/python3
def no_c(my_string):
    cp_str = ""
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        cp_str += x
    return cp_str
