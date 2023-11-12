import json
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
