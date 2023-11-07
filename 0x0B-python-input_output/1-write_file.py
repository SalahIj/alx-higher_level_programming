#!/usr/bin/python3
""" The module imported """


def write_file(filename="", text=""):
    """ The function definition """
    with open(filename, 'w', encoding="utf-8") as f:
        number = f.write(text)
        return (number)
