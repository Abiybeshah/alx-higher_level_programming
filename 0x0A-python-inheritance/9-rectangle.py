#!usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
"""Rectangle class that inherits from BaseGeo"""

    def __init__(self, width, height):
        """Method for init the attrubutes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Mthd to redefine a area mthd in the parent class"""

        return self.__width * self.__height

    def __str__(self):
        """__str__ metd for return the next str"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
