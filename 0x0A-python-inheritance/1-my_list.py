#!/usr/bin/python3
"""
Module wit class MyList
"""


class MyList(list):
    """MyList that inherits from list

    Args:
        list ([list]): List for display.
    """
    def print_sorted(self):
        """print_sorted
        display sorted list.
        """
        list_sorted = sorted(self)
        print(list_sorted)
