#!/usr/bin/python3
"""
a module that defines a Square class
"""


class Square:
    """
    a class with private instance attribute size and
    a public instance method: def area(self)
    that returns the current square area
    """
    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
