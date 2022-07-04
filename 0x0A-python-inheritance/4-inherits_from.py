#!/usr/bin/python3

"""Defines a function that Checks if obj is instance of a class that inherited from the specified class."""


def inherits_from(obj, a_class):
    """Checks if obj is instance of a class that inherited from the specified class."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
