#!/usr/bin/python3
"""
This is the module for Add two integers.
"""


def add_integer(a, b=98):
    """Sum of two integers
    Args:
        a: First Integer
        b: Second Integer
    Raises:
        TypeError: If a or b are not an integer o float.
    Returns:
        Result of sum.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
