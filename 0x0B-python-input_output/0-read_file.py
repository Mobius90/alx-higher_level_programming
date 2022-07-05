#!/usr/bin/python3

"""Defines a file reading function"""


def read_file(filename=""):
    """A function that reads file and prints"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
