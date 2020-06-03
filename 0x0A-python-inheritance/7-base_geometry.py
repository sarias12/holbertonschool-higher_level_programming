#!/usr/bin/python3
"""
Module With BaseGeometry Class
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
            name (str): Arugment for name of base Geometry
            value (int): Arfument for Value of base Geometry.

        Raises:
            TypeError: When value is not a integer.
            ValueError: When Value is less or equal to Zero.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
