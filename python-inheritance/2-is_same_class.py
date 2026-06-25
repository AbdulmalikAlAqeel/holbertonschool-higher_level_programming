#!/usr/bin/python3
"""This module contains a function that checks object types."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a specified class."""
    return type(obj) is a_class
