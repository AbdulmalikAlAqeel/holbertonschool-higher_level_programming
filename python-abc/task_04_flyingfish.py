#!/usr/bin/python3
"""
Module exploring multiple inheritance through Fish, Bird, and FlyingFish.
"""


class Fish:
    """Class representing a fish and its capabilities."""

    def swim(self):
        """Print the swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print the natural habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird and its capabilities."""

    def fly(self):
        """Print the flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Print the natural habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish that inherits from both Fish and Bird.
    """

    def swim(self):
        """Override the swim behavior for the flying fish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override the fly behavior for the flying fish."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override the habitat behavior for the flying fish."""
        print("The flying fish lives both in water and the sky!")
