#!/usr/bin/python3
"""divided matrice function"""


from cmath import inf


def matrix_divided(matrix, div):
    """ divided by div elemnt in matix
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) != int and type(i) != float:
                raise TypeError(("matrix must be a matrix "
                                "(list of lists) of integers/floats"))
    new_matix = []
    for array in matrix:
        page = []
        for elmt in array:
            if type(div) == float('inf'):
                elmt = 0.0
            else:
                elmt /= div
                elmt = round(elmt, 2)
                page.append(elmt)
        new_matix.append(page)
    return new_matix
