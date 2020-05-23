#!/usr/bin/python3
"""
This is the module that prints a square with the character # .
"""


def print_square(size):
    """print_square [summary]

    Args:
        size (int): Size or square

    Raises:
        TypeError: Size is not a integer number.
        ValueError: Size is a negative number.
        TypeError:Size is not a positive integer number.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for x in range(size):
        for y in range(size):
            print("{}".format('#'), end="")
        print()
