#!/usr/bin/python3
""" The module imported """


def append_after(filename="", search_string="", new_string=""):
    """ The function description:
    Args:
        filename: the first input
        search_string: the second input
        new_string: the third input
    Return:
        the result
    """
    tem = ""
    with open(filename, 'r', encoding="utf-8") as File:
        for i in File:
            tem += i
            if (search_string in i):
                tem += new_string

    with open(filename, 'w', encoding="utf-8") as File:
        File.write(tem)
