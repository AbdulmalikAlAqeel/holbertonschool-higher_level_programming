#!/usr/bin/python3
"""
This module contains a function that creates a Python Object
from a JSON file.
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a 'JSON file'.

    Args:
        filename (str): The name or path of the JSON file to read.

    Returns:
        any: The corresponding Python data structure.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
