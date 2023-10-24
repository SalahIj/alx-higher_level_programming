#!/usr/bin/python3
""" Class of square """


class Square:
    """ Definition of the class """

    def __init__(self, size=0, position=(0, 0)):
        """ Constractor:

        Args:
            size: the first input
            position: the second input
        """
        self._size = size
        self._position = position

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

    @property
    def position(self):
        return (self._position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(a, int) for a in value)
                or not all(a >= 0 for a in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

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
            print("")
            return
        if (self._position[1] > 0):
            for i in range(self._position[1]):
                print("")
        for i in range(self._size):
            for k in range(self._position[0]):
                print(" ", end="")
            for j in range(self._size):
                print("#", end="")
            print()
