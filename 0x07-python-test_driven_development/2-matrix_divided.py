#!/usr/bin/python3
""" Divides a matrix by a given value """


def matrix_divided(matrix, div):
    """ matrix_divided - Divides matrix by div """
    n_matrix = []
    x_len = len(matrix[0])

    if (div is 0):
        raise ZeroDivisionError("division by zero")
    if (type(div) is not int and type(div) is not float):
            raise TypeError("div must be a number")

    for x_coord in matrix:
        if (x_len != len(x_coord)):
            raise TypeError("Each row of the matrix must have the same size")

        new_x = []

        for value in x_coord:
            if (type(value) is not int and type(value) is not float):
                err_msg = "matrix must be a matrix "
                raise TypeError(err_msg + "(list of lists) of integers/floats")

            new_x.append(round(value / div, 2))

        n_matrix.append(new_x)

    return n_matrix
