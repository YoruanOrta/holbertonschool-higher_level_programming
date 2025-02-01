#!/usr/bin/python3
"""Module for Rectangle class."""


class Rectangle:
    """This class defines a simple Rectangle."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Creates a new instance of Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        self.print_symbol = "#"
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([
            str(self.print_symbol) * self.width for _ in range(self.height)
            ])

    def __repr__(self):
        """Return a string representation of the Rectangle for reproduction."""
        return "Rectangle({}, {})".format(self.width, self.height)

    @property
    def print_symbol(self):
        """Retrieve the value of print_symbol."""
        return self.__print_symbol

    @print_symbol.setter
    def print_symbol(self, value):
        """Set the value of print_symbol."""
        self.__print_symbol = value

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
