import json
import os
""" imported module """


class Base:
    """ The class definition """
    __nb_objects = 0

    def __init__(self, id=None):
        """ The constructor method:
        Args:
            id: the input of the function
        """
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
        string = "[]"
        if (not json_string or json_string is None):
            return (string)
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
