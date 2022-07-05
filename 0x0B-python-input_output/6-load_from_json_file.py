#!/usr/bin/python3
"""load from json file"""

import json


def load_from_json_file(filename):
    """create object from json file"""
    with open(filename, encoding='utf-8') as file:
        return (json.loads(file.read()))
