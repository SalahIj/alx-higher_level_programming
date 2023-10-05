#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if (a >= b):
        return (add(a, b))
    else:
        c = add(a, b)
        for j in range(4, 6):
            c = add(c, j)
            return (c)
        return (0)
