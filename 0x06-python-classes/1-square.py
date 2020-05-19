#!/usr/bin/python3
"""Class that defines a square."""


class Square:
    """Defining attributes for instance of Square Class.

    Args:
        size (int): Parameter indicating the size of the square.

    Attributes:
        size (int): size of the square.

    Returns:
        Nothing.
    """
    def __init__(self, size):
        self.__size = size
