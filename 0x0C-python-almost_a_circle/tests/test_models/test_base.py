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

    def test_Setting_Up(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id_testing(self):
        """ Testing assigning to id """
        A = Base(1)
        self.assertEqual(A.id, 1)

    def test_id_default_testing(self):
        """ Testing the default id """
        A = Base()
        self.assertEqual(A.id, 2)

    def test_id_nb_objects_testing(self):
        """ Testing the number of objects attributes """
        A = Base()
        B = Base()
        C = Base()
        self.assertEqual(A.id, 5)
        self.assertEqual(B.id, 6)
        self.assertEqual(C.id, 7)

    def test_id_default_testing(self):
        """ Testing the default id """
        A = Base()
        self.assertEqual(A.id, 2)

    def test_id_nb_objects_testing(self):
        """ Testing the number of objects attributes """
        A = Base()
        B = Base()
        C = Base()
        self.assertEqual(A.id, 3)
        self.assertEqual(B.id, 4)
        self.assertEqual(C.id, 5)

    def test_string_id_testing(self):
        """ Testing string id value """
        A = Base('1')
        self.assertEqual(A.id, '1')

    def test_more_args_id_testing(self):
        """ Testing the case when passing more
        args to init method
        """
        with self.assertRaises(TypeError):
            A = Base(1, 1)

    def test_access_private_attrs_testing(self):
        """ Testing accessing privates attributes """
        A = Base()
        with self.assertRaises(AttributeError):
            A.__nb_objects

    def test_save_to_file_square_testing(self):
        """ Testing save_to_file method for Square """
        Square.save_to_file(None)
        reste = "[]\n"
        with patch('sys.stdout', new_callable=StringIO) as out:
            with open("Square.json", "r") as File:
                print(File.read())
            self.assertEqual(out.getvalue(), reste)
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as File:
            self.assertEqual(File.read(), "[]")

    def test_save_to_file_rectangle_testing(self):
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
