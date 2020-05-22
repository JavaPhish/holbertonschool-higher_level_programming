#!/usr/bin/python3
""" Unittest for max_integer([..]) """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test cases for pyfile 6-max_integer.py """

    def test_base_use(self):
        """ test_base - Basic test, aka normal usage test """
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7]), 7)

    def test_empty_list(self):
        """ Pass an empty list """
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """ Negative numbers in the list """
        self.assertEqual(max_integer([1, 2, -3, -4, -5, -6]), 2)

    def test_one_value_in_list(self):
        """ only one value in an array """
        self.assertEqual(max_integer([1]), 1)

    def test_floats(self):
        """ Plugin floats cus why not """
        self.assertEqual(max_integer([1.0, 2.0, 3.3, 4.4, 5.5, 60.6, 1, 6, 0]), 60.6)

    def test_duplicate_values(self):
        """ More than one of the same value in an array """
        self.assertEqual(max_integer([1, 1, 1, 2, 2, 2, 3, 3, 3, 0, 0, 0, 0, 0]), 3)

    def test_one_neg_value(self):
        """ one value that's negative """
        self.assertEqual(max_integer([-3]), -3)
