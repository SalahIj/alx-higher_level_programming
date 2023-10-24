#!/usr/bin/python3
""" Class of square """


class Square:
    """ Definition of the class """

    def __init__(self, size=0):
        """ Constractor:

        Args:
            size: the first input
        """
        self._size = size

    @property
    def size(self):
        """ Property:

        Return:
            The result
        """
        return (self._size)

    @size.setter
    def size(self, value):
        """ Setter:

        Args:
            value: first input

        Return:
            The result
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Function:

        Return:
            The result
        """
        return (self._size ** 2)

    def my_print(self):
        """Function:
        """
        if (self._size == 0):
            print()
        else:
            for i in range(self._size):
                print("#" * self._size)
