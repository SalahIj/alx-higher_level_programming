#!/usr/bin/python3
""" The module imported """


def read_file(filename=""):
    """ The definiton of the function """
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
        print(data, end='')
