#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for string in row:
            if string == row[-1]:
                print("{:d}".format(string), end='')
            else:
                print("{:d}".format(string), end=' ')
        print()
