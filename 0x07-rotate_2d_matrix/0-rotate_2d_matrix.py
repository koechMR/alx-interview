#!/usr/bin/python3
""" Rotate 2D Matrix in"""


def rotate_2d_matrix(matrix):
    """Rotate it 90 degrees clockwise
    """
    # Replica of the Matrix
    replica = matrix[:]

    for i in range(len(matrix)):
        column = [row[i] for row in replica]
        matrix[i] = column[::-1]
