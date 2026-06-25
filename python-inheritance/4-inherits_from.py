#!/usr/bin/python3
"""This module defines a subclass-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a specified class.

    Returns True if the object's class is a subclass of a_class,
    excluding the class itself.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
