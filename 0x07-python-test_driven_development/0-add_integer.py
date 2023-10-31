#!/usr/bin/pytohn3
def add_integer(a, b=98):
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, float) and not isinstance(b, int)):
        raise TypeError("b must be an integer")
    if (type(a) == float):
        a = int(a)
    if (type(b) == float):
        b = int(b)
    return (a + b)
