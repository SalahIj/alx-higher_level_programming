#!/usr/bin/python3
""" Imported modeule """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ The class definition """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor:
        Args:
            size: the first input
            x: the second input
            y: the third input
            id: the firth input
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Str method:
        Return:
            the result
        """
        str_1 = "[{}] ".format(__class__.__name__)
        str_2 = "({}) ".format(self.id)
        str_3 = "{}/{} - ".format(self.x, self.y)
        str_4 = "{}".format(self.width)
        str_5 = str_1 + str_2 + str_3 + str_4
        return (str_5)

    @property
    def size(self):
        """ getter """
        return (self.width)

    @size.setter
    def size(self, value):
        """ setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update method:
        Args:
            args: the first input
            kwargs: the second
        """
        args_list = ['id', 'size', 'x', 'y']
        lenght = len(args)
        if (args is None or lenght == 0):
            for cle, valeur in kwargs.items():
                setattr(self, cle, valeur)
        else:
            for r in range(lenght):
                setattr(self, args_list[r], args[r])

    def to_dictionary(self):
        """ Dict method:
        Return:
            the result
        """
        dic = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return (dic)
