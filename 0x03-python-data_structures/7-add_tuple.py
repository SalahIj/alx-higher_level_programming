#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenght_a = len(tuple_a)
    lenght_b = len(tuple_b)
    a = tuple_a[0] if (lenght_a > 0) else 0
    b = tuple_a[1] if (lenght_a > 1) else 0
    A = tuple_b[0] if (lenght_b > 0) else 0
    B = tuple_b[1] if (lenght_b > 1) else 0
    return (a + A, b + B)
