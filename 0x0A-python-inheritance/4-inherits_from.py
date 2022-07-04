#!/usr/bin/python3
"""Defines a function that checks if an object is inherited instance of a class."""


def inherits_from(obj, a_class):
    """Checks if an object is inherited instance of a class.
    Args:
        obj (any): Object to check
        a_class (type): Class to match obj with
    Returns:
        bool: True if obj is inherited instance of class else False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
