#!/usr/bin/python3
""" The module imported """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ The class definition """
    def __init__(self, size):
        """ The function definition """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
