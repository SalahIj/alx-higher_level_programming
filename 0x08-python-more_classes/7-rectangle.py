#!/usr/bin/python3
""" rectangle class """


class Rectangle:
    """ Definition of a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self._height = height
        self._width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Definition of getter function for width """
        return (self._width)

    @width.setter
    def width(self, value):
        """ Definition of width setter function """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """ property function for height """
        return (self._height)

    @height.setter
    def height(self, value):
        """ setter function for height """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """ Definition of area function """
        return (self._height * self._width)

    def perimeter(self):
        """ Definition of perimeter function """
        if (self._height == 0 or self._width == 0):
            return (0)
        else:
            return (2 * (self._height + self._width))

    def __str__(self):
        """ Definition of str function """
        stri = ""
        if (self._width == 0 or self._height == 0):
            return (stri)
        else:
            for i in range(self._height):
                stri += "".join(str(self.print_symbol) * self._width)
                if (i != self._height - 1):
                    stri += "\n"
            return (stri)

    def __repr__(self):
        """ Representation function """
        return ("Rectangle({:d}, {:d})".format(self._width, self._height))

    def __del__(self):
        """ Deleting function for deleting an instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
