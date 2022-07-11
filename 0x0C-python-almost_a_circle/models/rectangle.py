#!/usr/bin/python3
"""Defines module of Rectangle class"""

from models.base import Base

class Rectangle(Base):
    """a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
