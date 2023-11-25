#!/usr/bin/python3
""" Classe defintiion """


def text_indentation(text):
    """ Function definition """
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    for aj in ".:?":
        text = (aj + "\n\n").join([line.strip(" ") for line in text.split(aj)])

    print("{}".format(text), end="")
