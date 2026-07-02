#!/usr/bin/python3
"""
This module contains a function that converts a Python data structure
to a JSON string representation.
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj (any): The Python object to be serialized.

    Returns:
        str: The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
