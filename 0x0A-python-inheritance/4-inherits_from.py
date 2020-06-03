#!/usr/bin/python3
"""
Module with function inherits_from
"""


def inherits_from(obj, a_class):
    """inherits_from [summary]

    Args:
        obj ([type]): [description]
        a_class ([type]): [description]

    Returns:
        [bool]: True if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class;
        otherwise False.
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
