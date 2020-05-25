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
    idx = 0
    while idx < len(text):
        print("{}".format(text[idx]), end="")
        if text[idx] == '.' or text[idx] == '?' or text[idx] == ':':
            print('\n')
            if text[idx + 1] == ' ':
                idx += 1
        idx += 1
