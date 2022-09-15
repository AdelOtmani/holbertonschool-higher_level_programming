#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for i in matrix:
        tmp = []
        for j in i:
            tmp.append(j**2)
        m.append(tmp)
    return m
