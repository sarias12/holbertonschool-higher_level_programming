#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary.has_key(key) == False:
        return a_dictionary
    else:
        del(a_dictionary[key])
        return a_dictionary
