#!/usr/bin/python3
"""
Module with function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class [summary]

    Args:
        obj: object
        a_class: instance

    Returns:
        [bool]: True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)
