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

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file [

        Args:
            list_objs (class): is a list of instances who inherits of Base.
        """
        new_list = []
        with open("{}.json".format(cls.__name__), 'w') as file_1:
            if list_objs is not None:
                for item in list_objs:
                    new_list.append(cls.to_dictionary(item))
            file_1.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string [summary]

        Args:
            json_string: string representing a list of dictionaries

        Returns:
            [str]: the list represented by json_string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
