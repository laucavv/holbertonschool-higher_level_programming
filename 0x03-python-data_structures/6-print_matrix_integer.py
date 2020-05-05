#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        l = 1
        for j in i:
            print("{:d}".format(j), end="")
            if len(i) > l:
                print(end=" ")
            l = l + 1
        print()
