#!/usr/bin/python3

"""Defines a function that checks if obj is instance of a class."""


def is_kind_of_class(obj, a_class):
    """Checks if is instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
