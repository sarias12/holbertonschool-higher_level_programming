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
    def width(self):
        """getter method for width

        Returns:
            [int]: [width attribute]
        """
        return self.__width

    @property
    def height(self):
        """getter method for height

        Returns:
            [int]: [height attribute]
        """
        return self.__height

    @width.setter
    def width(self, size):
        """setter method for width [summary]

        Args:
            width (int): square's width.

        Raises:
            TypeError: When the input(width) is not an integer.
            ValueError: When width is under or equals 0.
        """
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__width = size

    @height.setter
    def height(self, size):
        """setter method for height [summary]

        Args:
            height (int): square's height.

        Raises:
            TypeError: When the input(height) is not an integer.
            ValueError: When height is under or equals 0.
        """
        if type(size) is not int:
            raise TypeError("height must be an integer")
        if size <= 0:
            raise ValueError("height must be > 0")
        self.__height = size

    def update(self, *args, **kwargs):
        """method that assigns an argument to each attribute:
        1st argument - the id attribute
        2nd argument - the size attribute
        3th argument - the x attribute
        4th argument - the y attribute
        or that assigns a key/value argument to attributes.
        """
        if len(args) > 0:
            for idx, element in enumerate(args, 1):
                if idx == 1:
                    self.id = element
                if idx == 2:
                    self.size = element
                if idx == 3:
                    self.x = element
                if idx == 4:
                    self.y = element
        else:
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
