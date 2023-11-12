#!/usr/bin/python3
""" Module for test Base class """
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
import os


class TestBaseMethods(unittest.TestCase):
    """ Suite to test Base class """

    def Setting_Up(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def id_testing(self):
        """ Testing assigning to id """
        A = Base(1)
        self.assertEqual(A.id, 1)

    def id_default_testing(self):
        """ Testing the default id """
        A = Base()
        self.assertEqual(A.id, 1)

    def id_nb_objects_testing(self):
        """ Testing the number of objects attributes """
        A = Base()
        B = Base()
        C = Base()
        self.assertEqual(A.id, 1)
        self.assertEqual(B.id, 2)
        self.assertEqual(C.id, 3)

    def id_mix_testing(self):
        """ Testing the nb of objects attributes
        and assigning values to id
        """
        A = Base()
        B = Base(1024)
        C = Base()
        self.assertEqual(A.id, 1)
        self.assertEqual(B.id, 1024)
        self.assertEqual(C.id, 2)

    def string_id_testing(self):
        """ Testing string id value """
        A = Base('1')
        self.assertEqual(A.id, '1')

    def more_args_id_testing(self):
        """ Testing the case when passing more
        args to init method
        """
        with self.assertRaises(TypeError):
            A = Base(1, 1)

    def access_private_attrs_testing(self):
        """ Testing accessing privates attributes """
        A = Base()
        with self.assertRaises(AttributeError):
            A.__nb_objects

    def save_to_file_square_testing(self):
        """ Testing save_to_file method for Square """
        Square.save_to_file(None)
        reste = "[]\n"
        with open("Square.json", "r") as File:
            with patch('sys.stdout', A=StringIO()) as out:
                print(File.read())
                self.assertEqual(out.getvalue(), reste)
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as File:
            self.assertEqual(File.read(), "[]")

    def save_to_file_rectangle_testing(self):
        """ Test save_to_file method for Rectangle """
        Rectangle.save_to_file(None)
        reste = "[]\n"
        with open("Rectangle.json", "r") as File:
            with patch('sys.stdout', new=StringIO()) as out:
                print(File.read())
                self.assertEqual(out.getvalue(), reste)
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as File:
            self.assertEqual(File.read(), "[]")

    if __name__ == "__main__":
        unittest.main()
