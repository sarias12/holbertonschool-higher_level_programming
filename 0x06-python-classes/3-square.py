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
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """Defining attributes for instance of Square Class.

    Returns:
        Square area.
    """
    def area(self):
        return self.__size**2
