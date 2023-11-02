#!/usr/bin/pytohn3
"""
Simple doctest
test the deco
with 5 lines
"""


def add_integer(a, b=98):
    """
    add function
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, float) and not isinstance(b, int)):
        raise TypeError("b must be an integer")
    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)
    return (a + b)
