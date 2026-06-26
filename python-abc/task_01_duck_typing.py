#!/usr/bin/python3
"""This module explores abstract classes, interfaces, and duck typing."""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract Base Class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle."""

    def __init__(self, radius):
        """Initialize a new Circle instance.

        Args:
            radius (int, float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Return the calculated area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the calculated perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a new Rectangle instance.

        Args:
            width (int, float): The width of the rectangle.
            height (int, float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Return the calculated area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the calculated perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape object.

    This function utilizes duck typing, meaning it calls
    .area() and .perimeter() without explicitly checking
    the object's class type via isinstance.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
