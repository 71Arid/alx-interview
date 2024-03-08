#!/usr/bin/python3
"""
This module host the code that calculates pascals triangle
"""


def pascal_triangle(n):
    """
    pascals triangle function
    """
    matrix = [
        [1],
        [1, 1]
    ]
    if n == 1:
        matrix = [[1]]
        return matrix
    elif n == 2:
        return matrix
    else:
        i = 3
        while i <= n:
            new_row = []
            prev_row = matrix[i-2]
            new_column = len(prev_row)
            new_row.append(1)
            for j in range(1, new_column):
                new_row.append(prev_row[j-1] + prev_row[j])
            new_row.append(1)
            matrix.append(new_row)
            i = i + 1
        return matrix
