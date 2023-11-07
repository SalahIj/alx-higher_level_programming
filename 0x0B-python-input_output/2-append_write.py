#!/usr/bin/python3
""" The module imported: none """


def append_write(filename="", text=""):
    """ The function
    Args:
        filename: the first input
        text: the second input
    Return:
        the result
    """
    with open(filename, 'a', encoding="utf-8") as f:
        number_of_car = f.write(text)
        return (number_of_car)
