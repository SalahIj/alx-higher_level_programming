#!/usr/bin/python3
""" The module imported """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The class definition """
    def __init__(self, width, height):
        """ The defintion of the function """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ The function definition """
        return (self.__height * self.__width)

    def __str__(self):
        """ the function defifnition """
        return ("[Rectabgle] {}/{}".format(self.__width, self.__height))
