#!/usr/bin/python3
"""
This module defines a class Square.
It includes size validation, area calculation, and a visual print method.
"""


class Square:
    """
    A class that defines a square by its size and prints it using '#'.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of one side of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with strict validation.

        Args:
            value (int): The new size of the square side.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
