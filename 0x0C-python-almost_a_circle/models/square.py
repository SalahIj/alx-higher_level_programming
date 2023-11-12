from models.rectangle import Rectangle
""" Imported modeule """


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
        str_2 = "{} ".format(self.id)
        str_3 = "{}/{} - ".format(self.x, self.y)
        str_4 = "{}".format(self.width)
        return (str_1 + str_2 + str_3 + str_4)
