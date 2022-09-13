#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        j = " ".join([x.__str__() for x in i])
        print("{}".format(j))
