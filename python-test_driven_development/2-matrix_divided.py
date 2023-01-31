#!/usr/bin/python3
''' function that divides elements of matrix by div'''


def matrix_divided(matrix, div):
    ''' checking possibile errors and dividing'''
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    row_len = len(matrix[0])
    for i, row in enumerate(matrix):
        tmp = []
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for nr in row:
            if type(nr) not in [int, float]:
                type_err()
                return
            nr = int(nr)
            tmp.append(round(nr / div, 2))
        new_matrix.append(tmp)
    return new_matrix


def type_err():
    a = 'matrix must be a matrix (list of lists) of integers/floats'
    raise TypeError(a)
