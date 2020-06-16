#!/usr/bin/python3
"""
Rectangle Module
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__ initializig instance

        Args:
            width (int): Rectangle's width. Defaults to 0.
            height (int): Rectangle's height. Defaults to 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """area method

        Returns:
            [int]: the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """perimeter

        Returns:
            [int]: the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        """__str__

        Returns:
            [str]: Print the rectangle with the character "print_symbol".
        """
        text = ""
        if self.__width == 0 or self.__height == 0:
            return text
        for i in range(self.__height):
            for j in range(self.__width):
                text += str(self.print_symbol)
            if i != self.__height - 1:
                text += '\n'
        return text

    def __repr__(self):
        """__repr__

        Returns:
            [str]: string representation of the rectangle
            to be able to recreate a new instance.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """__del__ Delete instance
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal

        Args:
            rect_1 (obj): fisrt instance (object - rectangle type)
            rect_2 (obj): second instance (object - rectangle type)

        Raises:
            TypeError: when rect_1 is not a instance of Rectangle.
            TypeError: when rect_2 is not a instance of Rectangle.

        Returns:
            [obj]: returns the biggest rectangle
            based on the area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
