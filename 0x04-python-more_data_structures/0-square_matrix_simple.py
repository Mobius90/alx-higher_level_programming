#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    nmatrix = []
    for i in matrix:
        nmatrix.append([j**2 for j in i])
    return nmatrix
