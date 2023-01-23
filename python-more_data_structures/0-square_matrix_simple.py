#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for n1 in matrix:
        for n2 in n1:
            new_matrix.append(n2 * n2)
    return new_matrix
