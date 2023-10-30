#!/usr/bin/python3
""" rectangle class """


class Rectangle:
    """ Definition of a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Definition of getter function for width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Definition of width setter function """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ property function for height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ setter function for height """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Definition of area function """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Definition of perimeter function """
        if (self.__height == 0 or self.__width == 0):
            return (0)
        else:
            return (2 * (self.__height + self.__width))

    @classmethod
    def square(cls, size=0):
        """ Definition of function """
        return (Rectangle(size, size))

    def __str__(self):
        """ Definition of str function """
        stri = ""
        if (self.__width == 0 or self.__height == 0):
            return (stri)
        for i in range(self.__height):
            stri += "".join(str(self.print_symbol) * self.__width)
            if (i != self.__height - 1):
                stri += "\n"
        return (stri)

    def __repr__(self):
        """ Representation function """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

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
