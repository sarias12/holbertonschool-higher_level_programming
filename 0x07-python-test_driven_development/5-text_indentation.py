#!/usr/bin/python3
"""
This that prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """text_indentation [summary]

    Args:
        text (str): text for display in ouput.

    Raises:
        TypeError: when text is not a data type string.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print('\n')
            i += 1
        i += 1
