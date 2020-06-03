#!/usr/bin/python3
"""
Function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """lookup [summary]

    Args:
        obj (class): object for search attributes and methods.

    Returns:
        [list]: attributes and methods of an object.
    """
    return dir(obj)
