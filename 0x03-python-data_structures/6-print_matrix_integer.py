#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        i = 0
        for y in x:
            i += 1
            if i < len(x):
                print("{}".format(y), end=" ")
            else:
                print("{}".format(y))
