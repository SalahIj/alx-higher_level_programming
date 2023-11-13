#!/usr/bin/python3
""" Imported modules """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class Test_class_Rectangle(unittest.TestCase):
    def test_setUp(self):
        """ Instantiates class """
        Base._Base__nb_objects = 0

    def test_initialisation(self):
        """ Test intialisation """
        rect = Rectangle(10, 20, 30, 40, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 30)
        self.assertEqual(rect.y, 40)
        self.assertEqual(rect.id, 1)

    def test_a_class(self):
        """ Tests Rectangle instance. """
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle' > ")

    def test_Base_inheritance(self):
        """ Tests inheritance from Base. """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_with_no_args(self):
        """ Tests constructor signature. """
        with self.assertRaises(TypeError) as e:
            rect = Rectangle()
        srrt = "__init__() missing 2 required
        positional arguments: 'width' and 'height'"
        self.assertEqual(str(e.exception), srrt)

    def test_width_setter_testing(self):
        """ Tests the width setter """
        rect = Rectangle(10, 20, 30, 40, 1)
        rect.width = 15
        self.assertEqual(rect.width, 15)
        with self.assertRaises(TypeError):
            rect.width = "invalid"
        with self.assertRaises(ValueError):
            rect.width = 0

    def test_height_setter_testing(self):
        """ Tests the height setter """
        rect = Rectangle(10, 20, 30, 40, 1)
        rect.height = 25
        self.assertEqual(rect.height, 25)
        with self.assertRaises(TypeError):
            rect.height = "invalid"
        with self.assertRaises(ValueError):
            rect.height = 0

    def test_x_setter_testing(self):
        """ Tests x setter """
        rect = Rectangle(10, 20, 30, 40, 1)
        rect.x = 35
        self.assertEqual(rect.x, 35)
        with self.assertRaises(TypeError):
            rect.x = "invalid"
        with self.assertRaises(ValueError):
            rect.x = -5

    def test_y_setter_testing(self):
        """ Test the y setter """
        rect = Rectangle(10, 20, 30, 40, 1)
        rect.y = 45
        self.assertEqual(rect.y, 45)
        with self.assertRaises(TypeError):
            rect.y = "invalid"
        with self.assertRaises(ValueError):
            rect.y = -10

    def test_area_testing(self):
        """ Test the area method """
        rect = Rectangle(10, 20, 30, 40, 1)
        self.assertEqual(rect.area(), 200)

    def test_with_many_args(self):
        """ Tests constructor. """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        strr = "__init__() takes from 3 to 6
        positional arguments but 7 were given"
        self.assertEqual(str(e.exception), strr)

    def test_with_one_args(self):
        """ Tests constructor. """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        srt = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), srt)

    def test_Instantiation(self):
        """ Tests instantiation. """
        Base._Base__nb_objects = 0
        rect = Rectangle(10, 20)
        self.assertEqual(str(type(rect)),
                         "<class 'models.rectangle.Rectangle' > ")
        self.assertTrue(isinstance(rect, Base))
        da = {'_Rectangle__height': 20, '_Rectangle__width': 10,
              '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(rect.__dict__, da)
        with self.assertRaises(TypeError) as e:
            rect = Rectangle("1", 2)
        msg_1 = "width must be an integer"
        self.assertEqual(str(e.exception), msg_1)

        with self.assertRaises(TypeError) as e:
            rect = Rectangle(1, "2")
        msg_2 = "height must be an integer"
        self.assertEqual(str(e.exception), msg_2)

        with self.assertRaises(TypeError) as e:
            rect = Rectangle(1, 2, "3")
        msg_3 = "x must be an integer"
        self.assertEqual(str(e.exception), msg_3)

        with self.assertRaises(TypeError) as e:
            rect = Rectangle(1, 2, 3, "4")
        msg_4 = "y must be an integer"
        self.assertEqual(str(e.exception), msg_4)

        with self.assertRaises(ValueError) as e:
            rect = Rectangle(-1, 2)
        msg_5 = "width must be > 0"
        self.assertEqual(str(e.exception), msg_5)

        with self.assertRaises(ValueError) as e:
            rect = Rectangle(1, -2)
        msg_6 = "height must be > 0"
        self.assertEqual(str(e.exception), msg_6)

        with self.assertRaises(ValueError) as e:
            rect = Rectangle(0, 2)
        msg_7 = "width must be > 0"
        self.assertEqual(str(e.exception), msg_7)

        with self.assertRaises(ValueError) as e:
            rect = Rectangle(1, 0)
        msg_8 = "height must be > 0"
        self.assertEqual(str(e.exception), msg_8)

        with self.assertRaises(ValueError) as e:
            rect = Rectangle(1, 2, -3)
        msg_9 = "x must be >= 0"
        self.assertEqual(str(e.exception), msg_9)

        with self.assertRaises(ValueError) as e:
            rect = Rectangle(1, 2, 3, -4)
        msg_10 = "y must be >= 0"
        self.assertEqual(str(e.exception), msg_10)

    def test_positional_args(self):
        """ Tests positional args."""
        rect = Rectangle(5, 10, 15, 20, 1)
        da = {'_Rectangle__height': 10, '_Rectangle__width': 5,
              '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 1}
        self.assertEqual(rect.__dict__, da)
        rect = Rectangle(5, 10, 15, 20, 98)
        da = {'_Rectangle__height': 10, '_Rectangle__width': 5,
              '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 98}
        self.assertEqual(rect.__dict__, da)

    def test_keyword_args(self):
        """ Tests keywords args. """
        rect = Rectangle(100, 200, id=421, y=99, x=101)
        da = {'_Rectangle__height': 200, '_Rectangle__width': 100,
              '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(rect.__dict__, da)

    def test_inherited_id(self):
        """ Tests if id inherit from Base. """
        Base._Base__nb_objects = 98
        rect = Rectangle(2, 4)
        self.assertEqual(rect.id, 99)

    def test_properties(self):
        """ Tests property getters/setters. """
        rect = Rectangle(5, 9)
        rect.width = 100
        rect.height = 101
        rect.x = 102
        rect.y = 103
        da = {'_Rectangle__height': 101, '_Rectangle__width': 100,
              '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 102}
        self.assertEqual(rect.__dict__, da)
        self.assertEqual(rect.width, 100)
        self.assertEqual(rect.height, 101)
        self.assertEqual(rect.x, 102)
        self.assertEqual(rect.y, 103)

    def types_invalid(self):
        """ Returns tuple of types for validation. """
        tupl = (3.14, -1.1, float('inf'), float('-inf'), True,
                "str", (2,), [4], {5}, {6: 7}, None)
        return (tupl)

    def test_negative_value_gt(self):
        """ Tests properties of validation. """
        rect = Rectangle(1, 2)
        attrs = ["width", "height"]
        for i in attrs:
            a = "{} must be > 0".format(i)
        with self.assertRaises(ValueError) as e:
            setattr(rect, i, -(randrange(10) + 1))
        self.assertEqual(str(e.exception), a)

    def test_negative_value_ge(self):
        """ Tests properties of validation. """
        rect = Rectangle(1, 2)
        attrs = ["x", "y"]
        for i in attrs:
            a = "{} must be >= 0".format(i)
        with self.assertRaises(ValueError) as e:
            setattr(rect, i, -(randrange(10) + 1))
        self.assertEqual(str(e.exception), a)

    def test_zero_value(self):
        """ Tests properties validation. """
        rect = Rectangle(1, 2)
        attrs = ["width", "height"]
        for i in attrs:
            a = "{} must be > 0".format(i)
        with self.assertRaises(ValueError) as e:
            setattr(rect, i, 0)
        self.assertEqual(str(e.exception), a)

    def test_property_of_H(self):
        """ Tests properties of setting/getting. """
        rect = Rectangle(1, 2)
        attrs = ["x", "y", "width", "height"]
        for i in attrs:
            n = randrange(10) + 1
            setattr(rect, i, n)
            self.assertEqual(getattr(rect, i), n)

    def test_property_range_zero_of_H(self):
        """ Testing properties of setting/getting. """
        rect = Rectangle(1, 2)
        rect.x = 0
        rect.y = 0
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
