#!/usr/bin/python3
def puis(x):
    return (x ** 2)


def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(puis, submatrix)) for submatrix in matrix]
    return (new_matrix)
