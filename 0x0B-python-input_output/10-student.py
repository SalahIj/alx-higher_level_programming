#!/usr/bin/python3
""" The module imported """


class Student:
    """ Class description """
    def __init__(self, first_name, last_name, age):
        """ The function description:
        Args:
            first_name: the first input
            last_name: the second input
            age: the third input
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ The function description:
        Args:
            attrs: the input of the function
        Return:
            the result
        """
        if (attrs is None):
            return (self.__dict__)
        for i in attrs:
            if (type(i) is not str):
                return (self.__dict__)

        my_dictionary = dict()
        for cle, value in self.__dict__.items():
            if cle in attrs:
                my_dictionary[cle] = value
        return (my_dictionary)
