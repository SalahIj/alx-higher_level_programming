#!/usr/bin/python3
""" The module imported """


class BaseGeometry:
    """ The class definition """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise TypeError("{} must be greater than 0".format(name))
