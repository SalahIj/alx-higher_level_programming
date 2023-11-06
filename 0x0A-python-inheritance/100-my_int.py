#!/usr/bin/python3
""" The module imported """


class MyInt(int):
    """ the class definition """
    def __creat__(cls, *ars, **Kwar):
        return (super(MyInt, cls).__creat__(cls, *args, **Kwar))

    def __egal__(self, number):
        return (int(self) != number)

    def __inegal__(self, number):
        return (int(self) == number)
