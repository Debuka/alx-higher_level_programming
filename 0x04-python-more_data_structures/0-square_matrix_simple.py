#!/usr/bin/python3
# computes square value of the integers in a matrix
def square_matrix_simple(matrix=[]):
    mx = matrix.copy()
    for i in range(len(matrix)):
        mx[i] = list(map(lambda x: x**2, matrix[i]))
    return (mx)
