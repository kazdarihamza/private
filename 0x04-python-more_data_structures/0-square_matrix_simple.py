#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    return list(list(map(lambda a: a*a, numbers)) for numbers in matrix)
