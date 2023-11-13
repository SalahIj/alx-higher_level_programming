#!/usr/bin/python3
import json
import os
import csv
""" imported module """


class Base:
    """ The class definition """

    __nb_objects = 0

    def __init__(self, id=None):
        """ The constructor method: """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
