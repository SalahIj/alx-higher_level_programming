#!/usr/bin/python3
""" The module imported """


def inherits_from(obj, a_class):
    """ The function definition """
    if (isinstance(obj, a_class) and type(obj) is not a_class):
        return (True)
    else:
        return (False)
