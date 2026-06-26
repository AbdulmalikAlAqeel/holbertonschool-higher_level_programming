#!/usr/bin/python3
"""Module for Shape, Circle, Rectangle and shape_info."""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class Shape."""

    @abstractmethod
    def area(self):
        """Method for area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Method for perimeter."""
        pass


class Circle(Shape):
    """Class Circle."""

    def __init__(self, radius):
        """Constructor."""
        self.radius = radius

    def area(self):
        """Method for area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Method for perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class Rectangle."""

    def __init__(self, width, height):
        """Constructor."""
        self.width = width
        self.height = height

    def area(self):
        """Method for area."""
        return self.width * self.height

    def perimeter(self):
        """Method for perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Function shape_info."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
