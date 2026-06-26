#!/usr/bin/python3
"""
Module demonstrating the use of Mixins to compose class behaviors
modularly without rigid inheritance hierarchies.
"""


class SwimMixin:
    """Mixin class providing swimming functionality."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class providing flying functionality."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class representing a Dragon, composed of SwimMixin and FlyMixin
    behaviors, along with its own native actions.
    """

    def roar(self):
        """Print the unique roar behavior of the dragon."""
        print("The dragon roars!")
