#!/usr/bin/python3
"""Defines a Rectangle"""

class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """

    @property
    def width(self):
        """Get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle"""
        return self.__height

    @height
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("heighr must be >- 0")
        self.__height = value

   def area(self):
       """Return the area of the rectabgle"""
       return (self.__width * self.__height)

   def perimeter(self):
       """Return the area of the rectangle"""
       if self.__width == 0 or self.__height == 0:
           return (0)

   def __str__(self):
       """Return the printable repr of the rectangle
       Represents the rectangle with a # char
       """
       if self.__width == 0 or self.__height == 0:
           return ("")

       rect = []
       for i in range(self.__height):
           [rect.append('#') for j in range(self.__width)]
           if i != self.__height - 1:
               rect.append("\n")
       return ("".join(rect))
