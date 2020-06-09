#!/usr/bin/python3
"""
Rectagle Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square [summary]

    Args:
        Base (class): object from which it inherits Square Class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """__init__ [summary]

        Args:
            size (int): First attribute for a Square.
            x (int): Second attribute for a Square. Defaults to 0.
            y (int): Third attribute for a Square. Defaults to 0.
            id (int): Fourth attribute for a Square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Method for returns a string

        Returns:
            [str]: method so that it returns
            [Square] (<id>) <x>/<y> - <width>
        """
        out = "[Square] ({}) {}/{} - {}"
        return (out.format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """getter method for size

        Returns:
            [int]: [size attribute]
        """
        return self.width

    @size.setter
    def size(self, size):
        """setter method for size [summary]

        Args:
            size (int): square's size.
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """method that assigns an argument to each attribute:
        1st argument - the id attribute
        2nd argument - the size attribute
        3th argument - the x attribute
        4th argument - the y attribute
        or that assigns a key/value argument to attributes.
        """
        if len(args) > 0:
            for idx, element in enumerate(args):
                if idx == 0:
                    self.id = element
                if idx == 1:
                    self.size = element
                if idx == 2:
                    self.x = element
                if idx == 3:
                    self.y = element
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """to_dictionary [summary]

        Returns:
            [dict]: returns the dictionary representation of a Square.
        """
        dictionary = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'size': self.size,
        }
        return dictionary
