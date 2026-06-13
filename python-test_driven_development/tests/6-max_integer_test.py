#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test with a list of ordered integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with a list of unordered integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with the max integer at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """Test with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(max_integer([-1, -5, -2, -10]), -1)

    def test_floats(self):
        """Test with list of floats."""
        self.assertEqual(max_integer([1.5, 3.2, 0.5]), 3.2)
