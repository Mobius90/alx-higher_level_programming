#!/usr/bin/python3
"""module of 'Base' class"""

import json
import csv
import turtle


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
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 4, 1, 1, 98)
        if cls.__name__ == "Square":
            dummy = cls(2, 1, 1, 98)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(str(cls.__name__) + ".json", "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def load_from_file(cls):
        """retrieve a list of instances"""
        filename = cls.__name__ + ".json"
        list_obj = []
        try:
            with open(filename, 'r') as f:
                datas = cls.from_json_string(f.read())
            for i, dic in enumerate(datas):
                list_obj.append(cls.create(**datas[i]))
        except IOError:
            pass
        return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write the CSV serialization of a list of objects to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    csv_writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    csv_writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        """return a list of classes instantiated from a CSV file."""
        objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                o = cls.create(**dic)
                objs.append(o)
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw Rectangles and Squares using the turtle module"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
