#!/usr/bin/python3
"""
    Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Devides all matrix elements and Return a new matrix
       Divide Matrix elements of matrtix
    """
    tyerror = "matrix must be a matrix (list of lists) of integers/floats"
    sizeerror = "Each row of the matrix must have the same size"

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if isinstance(matrix, list) and matrix:
        new_matrix = matrix.copy()
        first_el = len(new_matrix[0])
        for row in new_matrix:
            if isinstance(row, list) and row:
                if first_el == len(row):
                    for col in row:
                        if type(col) in [int, float]:
                            pass
                        else:
                            raise TypeError(tyerror)
                else:
                    raise TypeError(sizeerror)
            else:
                raise TypeError(tyerror)
        return([[round(i/div, 2) for i in row] for row in new_matrix[:]])
    else:
        raise TypeError(tyerror)
