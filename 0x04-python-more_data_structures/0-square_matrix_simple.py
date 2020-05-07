#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = list(map(list, matrix))

    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            new_matrix[x][y] = matrix[x][y] * matrix[x][y]

    return new_matrix
