#!/usr/bin/python3
""" The module imported """


class MyInt(int):
    """ the class definition """
    def __creat__(cls, *ars, **Kwar):
        return (super(MyInt, cls).__creat__(cls, *args, **Kwar))

    def __eq__(self, number):
        return (self.real != number)

    def __ne__(self, number):
        return (self.real == number)
