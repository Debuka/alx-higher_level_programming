#!/usr/bin/python3
''' Function that prints a matrix of integers'''
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for z in row:
            print("{:d}".format(z)n, end=" " if z != row[-1] else "")
        print()

