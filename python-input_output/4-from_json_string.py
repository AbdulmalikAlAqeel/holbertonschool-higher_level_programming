#!/usr/bin/python3
"""
This module contains a function that converts a JSON string
into a Python data structure.
"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        any: The corresponding Python data structure (dict, list, etc.).
    """
    return json.loads(my_str)
