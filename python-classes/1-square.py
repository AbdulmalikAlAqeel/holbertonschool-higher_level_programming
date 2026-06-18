#!/usr/bin/python3
"""
This module defines a class Square.
It includes a private instance attribute for the square's size.
"""


class Square:
    """
    A class that defines a square by its size.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of one side of the square.
        """
        self.__size = size
