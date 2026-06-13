#!/usr/bin/python3
"""
Module for 0-add_integer
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int, float): The first number.
        b (int, float): The second number, defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
