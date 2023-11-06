#!/usr/bin/python3
""" The module imported """


def add_attribute(obj, attr_name, attr_value):
    """ The function definition """
    if (hasattr(obj, "__dict__")):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
