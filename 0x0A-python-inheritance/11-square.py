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

    def area(self):
        """ The area function """
        return (self.__size ** 2)

    def __str__(self):
        """ The str method """
        return ("[{}] {}/{}".format(self.__class__.__name__,
                                    self.__size, self.__size))
