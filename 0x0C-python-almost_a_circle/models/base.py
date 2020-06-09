#!/usr/bin/python3
""" Base Module
"""


import json


class Base:
    """
    Base Superclass of Rectangle class and Square Class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__ method for inizilizating

        Args:
            id (int): number to identify instantiated objects.
            Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string [summary]

        Args:
            list_dictionaries ([type]): [description]

        Returns:
            [type]: [description]
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
