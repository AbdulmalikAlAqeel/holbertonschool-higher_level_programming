#!/usr/bin/python3
"""This module defines a custom list subclass."""


class MyList(list):
    """A custom list class providing sorting display capabilities."""

    def print_sorted(self):
        """Prints the list elements in an ascending sorted order."""
        print(sorted(self))
