#!/usr/bin/python3
"""Defines module of Rectangle class"""


from base import Base

class Rectangle(Base):
    """a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
