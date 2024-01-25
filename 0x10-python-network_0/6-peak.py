#!/usr/bin/python3
""" The necessery imported modules """


def find_peak(list_of_integers):
    """ The function definition
    Args:
        list_of_integers: the input of the function
    Return:
        the result
    """
    lis_t = list_of_integers
    if lis_t == []:
        return None
    size = len(lis_t)

    start, end = 0, size - 1
    while start < end:
        m = start + (end - start) // 2
        if lis_t[m] > lis_t[m - 1] and lis_t[m] > lis_t[m + 1]:
            return list_[m]
        if lis_t[m - 1] > lis_t[m + 1]:
            end = m
        else:
            start = m + 1
    return lis_t[start]
