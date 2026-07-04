#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates a list of lists of integers representing Pascal's Triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        
        # Calculate the internal values of the row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
            
        row.append(1)  # The last element is always 1
        triangle.append(row)

    return triangle
