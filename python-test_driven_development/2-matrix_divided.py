#!/usr/bin/python3
"""
Module 2-matrix_divided
Provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int, float): The number to divide by.

    Returns:
        list: A new matrix containing the results rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    # Verify that the matrix is a list of lists containing only numbers
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check that each row has the same size
    row_size = len(matrix[0]) if matrix else 0
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # Check the divisor type
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return a new matrix with elements divided and rounded to 2 decimal places
    return [[round(x / div, 2) for x in row] for row in matrix]
