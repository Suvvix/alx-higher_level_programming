#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Represents a rectangular shape."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with specified width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute and return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Compute and return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
