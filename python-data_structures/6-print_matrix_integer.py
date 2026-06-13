#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for row in matrix:
        for idx, num in enumerate(row):
            if idx != 0:
                print(" ", end="")
            print("{:d}".format(num), end="")
        print()
