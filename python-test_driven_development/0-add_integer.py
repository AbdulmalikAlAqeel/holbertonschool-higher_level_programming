#!/usr/bin/python3
"""
Module 0-add_integer
Provides a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int, float): The first number.
        b (int, float): The second number.

    Returns:
        int: The sum of a and b casted to int.

    Raises:
        TypeError: If a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to int before performing the addition
    return int(a) + int(b)
