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
        """ JSON representation:
        Args:
            list_dictionaries
        Return:
            the result
        """
        lenght = len(list_dictionaries)
        string = "[]"
        if (list_dictionaries is None or lenght == 0):
            return (string)
        else:
            return (json.dumps(list_dictionaries))
