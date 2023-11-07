#!/usr/bin/python3
""" The module imported """


class Student:
    """ The function description:
    Args:
        first_name: the first input
        last_name: the second input
        age: the third input
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ The function description:
        Return:
            the result
        """
        return (self.__dict__)
