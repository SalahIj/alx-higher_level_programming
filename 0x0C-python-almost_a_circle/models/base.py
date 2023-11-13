#!/usr/bin/python3
""" imported module """

import json
import os
import csv


class Base:
    """ The class definition """

    __nb_objects = 0

    def __init__(self, id=None):
        """ The constructor method: """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON representation method:
        Args:
            list_dictionaries: the input of the method
        Return:
            the result
        """
        lenght = len(list_dictionaries)
        string = "[]"
        if (list_dictionaries is None or lenght == 0):
            return (string)
        else:
            return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to list of json representation:
        Args:
            json_string: the input of the method
        Return:
            the result
        """
        lenght = len(json_string)
        if (json_string is None or lenght == 0):
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """ saving to file method:
        Args:
            cls: class
            list_objs: the second input
        """
        list_dictionary = []
        filename = "{}.json".format(cls.__name__)

        if (not list_objs):
            pass
        else:
            list_dictionary = [k.to_dictionary() for k in list_objs]
        List = cls.to_json_string(list_dictionary)
        with open(filename, 'w', encoding='utf-8') as File:
            File.write(List)

    @classmethod
    def create(cls, **dictionary):
        """ method """
        from models.rectangle import Rectangle
        from models.square import Square
        if (cls is Rectangle):
            dummy = Rectangle(1, 1)
        if (cls is Square):
            dummy = Square(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """ load method """
        filename = "{}.json".format(cls.__name__)
        list_in = []
        if (os.path.exists(filename) is False):
            return ([])
        with open(filename, 'r', encoding="utf-8") as File:
            data = File.read()
        List_in = [cls.create(**i) for i in cls.from_json_string(data)]
        return (List_in)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save in csv file method """
        filename = "{}.csv".format(cls.__name__)
        objects_list = []
        if (not list_objs):
            pass
        else:
            if (cls.__name__ == "Rectangle"):
                for o in list_objs:
                    objects_list.append([o.id, o.width, o.height, o.x, o.y])
            elif (cls.__name__ == "Square"):
                for o in list_objs:
                    objects_list.append([o.id, o.size, o.x, o.y])
        with open(filename, 'w', encoding='utf-8', newline='') as File:
            data = csv.writer(File)
            data.writerows(objects_list)

    @classmethod
    def load_from_file_csv(cls):
        """ Load from csv file method """
        filename = "{}.csv".format(cls.__name__)
        tab = []
        if (os.path.exists(filename) is False):
            return ([])
        with open(filename, 'r', encoding='utf-8', newline='') as File:
            data = csv.reader(File)
            for i in data:
                for index, r in enumerate(i):
                    i[index] = int(r)
                if (cls.__name__ == "Square"):
                    d = {"id": i[0], "size": i[1], "x": i[2], "y": i[3]}
                elif (cls.__name__ == "Rectangle"):
                    d = {"id": i[0], "width": i[1], "height": i[2],
                         "x": i[3], "y": i[4]}
                tab.append(cls.create(**d))
        return (tab)

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        tor = turtle.Turtle()
        ecran = turtle.Screen()
        tor.speed(5)
        tor.pensize(5)
        for i in list_rectangles:
            tor.penup()
            tor.goto(i.x, i.y)
            tor.color("black")
            tor.pendown()
            tor.forward(i.width)
            tor.left(90)
            tor.forward(i.height)
            tor.left(90)
            tor.forward(i.width)
            tor.left(90)
            tor.forward(i.height)

        for j in list_squares:
            tor.penup()
            tor.goto(j.x, j.y)
            tor.pendown()
            for colors in ["green", "blue", "purple", "red"]:
                tor.color(colors)
                tor.forward(j.size)
                tor.left(90)
        tor.penup()
        ecran.exitonclick()
