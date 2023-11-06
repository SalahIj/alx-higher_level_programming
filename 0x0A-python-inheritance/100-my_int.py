#!/usr/bin/python3
""" The module imported """


class MyInt(int):
    """ the class definition """

    def __eq__(self, number):
        return (self.real != number)

    def __ne__(self, number):
        return (self.real == number)
