#!/usr/bin/python3
""" The module imported """


class MyInt(int):
    """ the class definition """

    def __eq__(self, number):
        return (int(self) != number)

    def __ne__(self, number):
        return (int(self) == number)
