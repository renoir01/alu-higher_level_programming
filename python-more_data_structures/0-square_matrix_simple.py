#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = list(matrix)
    new_matrix = list()
    for row in copy_matrix:
        box = list()
        for column in row:
            box.append(column ** 2)
        new_matrix.append(box)
        del box
    return new_matrix
