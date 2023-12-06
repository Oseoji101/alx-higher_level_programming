#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    return [list(map(lambda x: x ** 2, lines)) for lines in matrix]
