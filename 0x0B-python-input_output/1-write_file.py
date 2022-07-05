#!/usr/bin/python3

"""Defines a file writing function"""


def write_file(filename="", text=""):
    """A function that writes string to text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
