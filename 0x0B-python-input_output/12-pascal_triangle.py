#!/usr/bin/python3
""" The module imported """


def pascal_triangle(n):
    """ The function description:
    Args:
        n: the input of the function
    Return:
        The result
    """
    List = []
    if (n <= 0):
        return (List)
    debut = [[1]]
    i = 0
    while (i is not n):
        j = 0
        while (j is not i + 1):
            if (j == 0):
                List.append([1])
            elif (j == i):
                List[i].append(1)
            else:
                List[i].append(List[i - 1][j] + List[i - 1][j - 1])
            j += 1
        i += 1
    return (List)
