#!/usr/bin/python3
"""
a module that defines a Square class
"""


class Square:
    """
    a class with private instance attribute size
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
