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
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position
    """Calculating area for instance of Square Class.

    Returns:
        Square area.
    """
    def area(self):
        return self.__size**2
    """Get attribute size"""
    @property
    def size(self):
        return self.__size
    """set attribute size."""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """Get attribute position"""
    @property
    def position(self):
        return self.__position
    """set attribute position"""
    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    """Printing in stdout the square with the character # according to the
    indicated position.

    Returns:
        Nothing
    """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] != 0:
                for x in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                print("{}".format(' ' * self.__position[0]), end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
