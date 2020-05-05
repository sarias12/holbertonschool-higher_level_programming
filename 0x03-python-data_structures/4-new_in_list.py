#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    clone_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return clone_list
    clone_list[idx] = element
    return clone_list
