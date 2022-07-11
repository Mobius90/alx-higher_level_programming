#!/usr/bin/python3
"""module of 'Base' class"""

import json


class Base:
    """Representation of a Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        text = []
        if list_objs is not None:
            for list1 in list_objs:
                text.append(list1.to_dictionary())
        with open(filename, mode='w', encoding="utf-8") as MyFile:
            return MyFile.write(Base.to_json_string(text))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            tmp = cls(10, 10)
        elif cls.__name__ == "Square":
            tmp = cls(10, 10)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(str(cls.__name__) + ".json", "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
