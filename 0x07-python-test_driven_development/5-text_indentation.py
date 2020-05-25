#!/usr/bin/python3
"""
This is the module that prints My name is <first name> <last name>
"""

def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print('\n')
            i += 1
        i += 1
    print()
