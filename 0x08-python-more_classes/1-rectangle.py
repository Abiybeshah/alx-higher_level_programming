#!/usr/bin/python3
"""Defines a rectangle class"""

class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle

        Args:
            width (int): The Width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Get/set the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
