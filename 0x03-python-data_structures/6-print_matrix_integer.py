#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for x in matrix:
            i = 0
            for y in x:
                i += 1
                if i < len(x):
                    print("{:d}".format(y), end=" ")
                else:
                    print("{:d}".format(y))
