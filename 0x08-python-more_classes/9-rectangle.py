#!/usr/bin/python3
""" rectangle class """


class Rectangle:
    """ Definition of a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Definition of getter function for width """
        return (self._width)

    @property
    def height(self):
        """ property function for height """
        return (self._height)

    @width.setter
    def width(self, value):
        """ Definition of width setter function """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @height.setter
    def height(self, value):
        """ setter function for height """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """ Definition of area function """
        return (self.height * self.width)

    def perimeter(self):
        """ Definition of perimeter function """
        if (self.height == 0 or self.width == 0):
            return (0)
        else:
            return (2 * (self.height + self.width))

    @classmethod
    def square(cls, size=0):
        """ Definition of function """
        return (Rectangle(size, size))

    def __str__(self):
        """ Definition of str function """
        stri = ""
        if (self.width == 0 or self.height == 0):
            return (stri)
        for i in range(self.height):
            stri += "".join(str(self.print_symbol) * self.width)
            if (i != self.height - 1):
                stri += "\n"
        return (stri)

    def __repr__(self):
        """ Representation function """
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """ Deleting function for deleting an instance """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Comparing areas function """
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return (rect_1)
        else:
            return (rect_2)
