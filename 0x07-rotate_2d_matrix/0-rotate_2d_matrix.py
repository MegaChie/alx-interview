#!/usr/bin/python3
"""Matrix manipulation"""


def rotate_2d_matrix(matrix):
    """Rotates the matrix 90 degrees to the right"""
    length = len(matrix)
    # Transpose the matrix
    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse order of raws
    for i in range(length):
        matrix[i].reverse()
