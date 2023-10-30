#!/usr/bin/python3
""" rectangle class """


class Rectangle:
    """ Definition of a rectangle """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """ proprety function for width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setter function for width """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Proprety function for height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter function for height """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
