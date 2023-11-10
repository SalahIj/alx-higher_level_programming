class Base:
    """ The Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Th contructor function:
        Args:
            id: the input of the method
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
