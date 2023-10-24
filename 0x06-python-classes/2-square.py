#!/usr/bin/python3
""" Square class """


class Square:
    """ Definition of the class """

    def __init__(self, Square__size=0):
        """Constractor:

        Args:
            Square__size: the first input

        Raises:
            ValueError: condition about signe
            TypeError: condition about type
        """
        if not isinstance(Square__size, int):
            raise TypeError("size must be an integer")
        if (Square__size < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = Square__size
