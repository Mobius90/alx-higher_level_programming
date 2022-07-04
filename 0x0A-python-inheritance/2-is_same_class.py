#!/usr/bin/python3

"""Defines a class checker function."""


def is_same_class(obj, a_class):
    """Checks if instance of a class."""
    if type(obj) == a_class:
        return True
    return False
