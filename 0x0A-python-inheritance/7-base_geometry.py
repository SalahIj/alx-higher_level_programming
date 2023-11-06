#!/usr/bin/python3
""" The module imported """


class BaseGeometry:
    """ The class definition """
    def area(self):
        """ Method number 1 """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method number 2 """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
