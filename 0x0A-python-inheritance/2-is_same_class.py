#!/usr/bin/python3
"""
Module with function is_same_class
"""


def is_same_class(obj, a_class):
    """is_same_class [summary]

    Args:
        obj: object
        a_class: instance

    Returns:
        [bool]: True if the object is exactly an instance of
        the specified class ; otherwise False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
