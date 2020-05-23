#!/usr/bin/python3
"""
This is the module that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """matrix_divided [summary]

    Args:
        matrix (list): list of list of integers or floats.
        div (int or float): number for division.

    Raises:
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to Zero.
        TypeError: The matrix is not a list of lists of integers or floats.
        TypeError: Any of the rows is  of a different size from the initial.
        TypeError: If the matrix is not a list of lists of integers or floats.

    Returns:
        list: new matrix (list of lists).
    """
    new_matrix = []
    alert = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    size = len(matrix[0])
    for y in matrix:
        if type(y) != list:
            raise TypeError(alert)
        if len(y) != size:
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for x in y:
            if type(x) != int and type(x) != float:
                raise TypeError(alert)
            new_list.append(round(x / div, 2))
        new_matrix.append(new_list)
    return new_matrix
