#!/usr/bin/python3
"""
pascal function that returns all lists of integers representing Pascal's triangle of n
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified number of rows.

    :param n: The number of rows in the Pascal's triangle.
    :return: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """
    Print the Pascal's triangle.

    :param triangle: The Pascal's triangle to be printed.
    """
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))
