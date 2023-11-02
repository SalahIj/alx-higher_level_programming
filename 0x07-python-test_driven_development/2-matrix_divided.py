#!/usr/bin/pyton3
"""
Import module
for the function
"""


def matrix_divided(matrix, div):
    """
    the definition of the function
    """

    message_1 = "matrix must be a matrix (list of lists) of integers/floats"
    message_2 = "Each row of the matrix must have the same size"

    if (type(matrix) is not list or len(matrix) == 0):
        raise TypeError(message_1)
    if (not isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    for ligne in matrix:
        if (type(ligne) is not list or len(ligne) == 0):
            raise TypeError(message_1)
        if (len(ligne) != len(matrix[0])):
            raise TypeError(message_2)
        for x in ligne:
            if (not isinstance(x, (int, float))):
                raise TypeError(message_1)
        return [[round(ind / div, 2) for ind in ligne] for ligne in matrix]
