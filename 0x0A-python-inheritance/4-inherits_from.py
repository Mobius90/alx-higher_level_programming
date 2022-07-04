#!/usr/bin/python3
"""Defines a function that checks if an object is inherited instance of a class."""


def inherits_from(obj, a_class):
    """checks if an object is inherited instance of a class.

    Args:
        obj (_type_): Object to check
        a_class (_type_): Class to match obj with

    Returns:
        bool: True if obj is inherited instance of class else False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
