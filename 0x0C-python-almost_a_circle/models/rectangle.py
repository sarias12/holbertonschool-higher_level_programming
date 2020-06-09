#!/usr/bin/python3
"""
Rectagle Module
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle [summary]

    Args:
        Base (class): object from which it inherits Rectagle Class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ [summary]

        Args:
            width (int): First attribute for a rectangule.
            height (int): Second attribute for a rectangule.
            x (int): Third attribute for a rectangule. Defaults to 0.
            y (int): fourth attribute for a rectangule. Defaults to 0.
            id (int): Fifth attribute for a rectangule. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

    @property
    def x(self):
        """getter method for x

        Returns:
            [int]: [x attribute]
        """
        return self.__x

    @property
    def y(self):
        """getter method for y

        Returns:
            [int]: [y attribute]
        """
        return self.__y

    @width.setter
    def width(self, width):
        """setter method for width [summary]

        Args:
            width (int): rectangle's width.

        Raises:
            TypeError: When the input(width) is not an integer.
            ValueError: When width is under or equals 0.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """setter method for height [summary]

        Args:
            height (int): rectangle's height.

        Raises:
            TypeError: When the input(height) is not an integer.
            ValueError: When height is under or equals 0.
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """setter method for x [summary]

        Args:
            x (int): rectangle's x.

        Raises:
            TypeError: When the input(x) is not an integer.
            ValueError: When x is under 0.
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """setter method for y [summary]

        Args:
            y (int): rectangle's y.

        Raises:
            TypeError: When the input(y) is not an integer.
            ValueError: When y is under 0.
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """method to calculate the area

        Returns:
            [int]: rectangle's area
        """
        return self.width * self.height

    def display(self):
        """Method prints in stdout the Rectangle
        instance with the character # by taking care of x and y.
        """
        for new_line in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Method for returns a string

        Returns:
            [str]: method so that it returns
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        out = "[Rectangle] ({}) {}/{} - {}/{}"
        return (out.format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """method that assigns an argument to each attribute:
        1st argument - the id attribute
        2nd argument - the width attribute
        3rd argument - the height attribute
        4th argument - the x attribute
        5th argument - the y attribute
        or that assigns a key/value argument to attributes.
        """
        if len(args) > 0:
            for idx, element in enumerate(args, 1):
                if idx == 1:
                    self.id = element
                if idx == 2:
                    self.height = element
                if idx == 3:
                    self.width = element
                if idx == 4:
                    self.x = element
                if idx == 5:
                    self.y = element
        else:
            if len(kwargs) > 0:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                    if key == 'height':
                        self.height = value
                    if key == 'width':
                        self.width = value
                    if key == 'x':
                        self.x = value
                    if key == 'y':
                        self.y = value

    def to_dictionary(self):
        """to_dictionary [summary]

        Returns:
            [dict]: returns the dictionary representation of a Rectangle.
        """
        dictionary = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
        return dictionary
