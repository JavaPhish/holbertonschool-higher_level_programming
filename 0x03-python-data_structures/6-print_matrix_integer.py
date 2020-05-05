#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for y in range(0, len(i)):
            print("{:d}".format(i[y]), end="")
            if (y is not len(i) - 1):
                print(" ", end="")
        print("")
