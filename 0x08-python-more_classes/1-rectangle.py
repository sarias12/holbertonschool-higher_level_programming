#!/usr/bin/python3
"""
Rectangle Module
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """__init__ initializig instance

        Args:
            width (int): Rectangle's width. Defaults to 0.
            height (int): Rectangle's height. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for width

        Returns:
            [int]: Rectangle's width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width

        Args:
            value (int): size of width

        Raises:
            TypeError: when value is not a integer.
            ValueError: when value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for height

        Returns:
            [int]: Rectangle's height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height

        Args:
            value (int): size of height

        Raises:
            TypeError: when value is not a integer.
            ValueError: when value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
