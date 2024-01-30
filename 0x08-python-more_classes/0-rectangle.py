#!/usr/bin/python3
"""
Defines an empty Rectangle class
"""

class Rectangle:

     @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

     @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    pass
