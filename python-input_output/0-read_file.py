#!/usr/bin/python3
"""
This module contains a function that reads a text file and prints its content.
It focuses on safe file handling using the 'with' statement.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name or path of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
