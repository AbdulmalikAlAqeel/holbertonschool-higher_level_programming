#!/usr/bin/python3
"""This module defines a class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or its subclass."""
    return isinstance(obj, a_class)
