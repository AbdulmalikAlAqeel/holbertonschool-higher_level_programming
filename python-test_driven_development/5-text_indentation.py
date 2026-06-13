#!/usr/bin/python3
"""
Module 5-text_indentation
Provides a function that prints text with 2 new lines after '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', and ':'.

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ".?:"
    formatted_text = text

    # Loop through each special character to indent
    for char in chars:
        # Split by the character and rebuild with two newlines
        formatted_text = (char + "\n\n").join(
            [line.strip() for line in formatted_text.split(char)]
        )

    # Print the result
    print(formatted_text, end="")
