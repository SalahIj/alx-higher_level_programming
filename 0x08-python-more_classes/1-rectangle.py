#!/usr/bin/python3
""" rectangle class """


class Rectangle:
    """ Definition of a rectangle """

    def __init__(self, Rectangle__width=0, Rectangle__height=0):
        self._Rectangle__height = Rectangle__height
        self._Rectangle__width = Rectangle__width

    @property
    def width(self):
        """ proprety function for width """
        return (self._Rectangle__width)

    @width.setter
    def width(self, value):
        """ setter function for width """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """ Proprety function for height """
        return (self._Rectangle__height)

    @height.setter
    def height(self, value):
        """ Setter function for height """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
