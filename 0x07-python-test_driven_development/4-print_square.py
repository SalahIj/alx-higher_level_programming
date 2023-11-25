#!/usr/bin/python3
""" Class definition """


def print_square(size):
    """ Function definition """

    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
