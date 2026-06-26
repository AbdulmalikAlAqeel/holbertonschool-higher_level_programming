#!/usr/bin/python3
"""
Module for geometry shapes, demonstrating abstract base classes
and duck typing in Python.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class that defines the interface for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete class representing a circle geometry.
    """

    def __init__(self, radius):
        """
        Initialize the circle with a specific radius.
        """
        self.radius = radius

    def area(self):
        """
        Return the area of the circle using math.pi.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Return the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a rectangle geometry.
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a given shape using duck typing.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
