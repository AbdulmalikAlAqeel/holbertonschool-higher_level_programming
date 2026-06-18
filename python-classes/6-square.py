#!/usr/bin/python3
"""
This module defines a class Square.
It includes size and position properties with validation,
along with area calculation and advanced printing capabilities.
"""


class Square:
    """
    A class that defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square sides. Defaults to 0.
            position (tuple): The coordinates of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: A tuple of 2 positive integers representing the coordinates.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with strict validation.

        Args:
            value (tuple): The new coordinates of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using the '#' character, taking into account
        the horizontal and vertical offsets specified by the position attribute.
        """
        if self.__size == 0:
            print()
            return

        # 1. Print the vertical space (newlines) using position[1]
        for _ in range(self.__position[1]):
            print()

        # 2. Print the square rows with horizontal spaces using position[0]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
