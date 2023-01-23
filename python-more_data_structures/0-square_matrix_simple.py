#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for _list in matrix:
        tmp = []
        for nr in _list:
            tmp.append(nr * nr)
        new_matrix.append(tmp)
    return new_matrix
