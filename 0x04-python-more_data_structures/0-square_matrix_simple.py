#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_ma = [i[:] for i in matrix]
    idx = 0
    for row in new_ma:
        for j in row:
            row[idx] = j ** 2
            idx += 1
        idx = 0
    return (new_ma)
