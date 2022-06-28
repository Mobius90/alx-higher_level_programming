#!/usr/bin/python3
"""
This module defines `add_integer`
"""


def add_integer(a, b=98):
    """
    adds a and b
    """
    values = []
    for x, param in [(a, 'a'), (b, 'b')]:
        if isinstance(x, int):
            values.append(x)
        elif isinstance(x, float):
            values.append(int(x))
        else:
            raise TypeError("{} must be an integer".format(param))
    return sum(values)
