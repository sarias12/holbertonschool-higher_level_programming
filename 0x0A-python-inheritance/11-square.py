#!/usr/bin/python3
"""
Module With BaseGeometry Class and Rectangle Subclass.
"""


class BaseGeometry():
    """BaseGeometry Class with Methods area and integer_validator
    """
    def area(self):
        """area method with Exception.

        Raises:
            Exception: While area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator [summary]

        Args:
            name (str): Arugment for attribute's name of base Geometry
            value (int): Argument for Value of base Geometry.

        Raises:
            TypeError: When value is not a integer.
            ValueError: When Value is less or equal to Zero.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle

    Args:
        BaseGeometry (class): from where will inherit Rectangle Subclass.
    """
    def __init__(self, width, height):
        """__init__ [summary]

        Args:
            name (str): Arugment for attribute's name of base Geometry
            value (int): Argument for Value of base Geometry.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area [summary]

        Returns:
            [int]: Area of a Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """__str__ display rectangle.
        """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """Square [summary]

    Args:
        Rectangle (class): from where will inherit square Subclass.
    """
    def __init__(self, size):
        """__init__ [summary]

        Args:
            size (int): Size of square.
        """
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """__str__ display square.
        """
        return("[Square] {}/{}".format(self.__size, self.__size))
