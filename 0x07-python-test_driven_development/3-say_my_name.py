#!/usr/bin/python3
"""
This is the module that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """say_my_name [summary]

    Args:
        first_name (str): First Argument for display
        last_name (str, optional): Second argument for display. Defaults to "".

    Raises:
        TypeError: when first name (argument) is not string data type
        TypeError: when second name (argument) is not string data type
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
