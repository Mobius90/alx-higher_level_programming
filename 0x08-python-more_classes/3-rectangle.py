#!/usr/bin/python3
"""
a module that defines a Rectangle class
"""


class Rectangle:
    """
    defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        returns # for the printable representation of the Rectangle
        """
        a = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(self.__height):
            a = a + ("#" * self.__width)
            if i is not self.__height - 1:
                a = a + "\n"
        return a
adsfa sdfasdfasdfasd