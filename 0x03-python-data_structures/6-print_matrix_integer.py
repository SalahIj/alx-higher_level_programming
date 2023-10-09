#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return (None)
    for i in matrix:
        if (len(i) == 0):
            print()
        for index, j in enumerate(i):
            print("{:d}".format(j), end="\n" if index == len(i) - 1 else " ")
