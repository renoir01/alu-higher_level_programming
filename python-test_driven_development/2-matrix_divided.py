#!/usr/bin/python3
"""
a function that divides all elements of a matrix.

Prototype: def matrix_divided(matrix, div)

All elements of the matrix should be divided by div,

rounded to 2 decimal places.

Returns a new matrix.

You are not allowed to import any module.
"""


def matrix_divided(matrix, div):
    """
    matrix must be a list of lists of integers or floats,

    otherwise raise a TypeError exception with the message

    matrix must be a matrix (list of lists) of integers/floats.

    Each row of the matrix must be of the same size,

    otherwise raise a TypeError exception with the message

    Each row of the matrix must have the same size.

    div must be a number (integer or float), otherwise

    otherwise raise a ZeroDivisionError exception with

    the message division by zero.
    """
    matrix_copy = list(matrix)
    try:
        if matrix_copy == []:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        elif not isinstance(div, int) and not isinstance(div, float):
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError("division by zero")
        for height in matrix_copy:
            if not isinstance(height, list):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            for value in height:
                if not isinstance(value, int) and not \
                        isinstance(value, float):
                    raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
                else:
                    continue
        sizes = []
        for row in matrix_copy:
            sizes.append(len(row))
        if len(set(sizes)) != 1:
            raise TypeError("Each row of the matrix must have the same size")
    except TypeError:
        raise
    except ZeroDivisionError:
        raise
    else:
        new_matrix = []
        for my_list in matrix_copy:
            new_list = []
            for digit in my_list:
                new_list.append(round(digit / div, 2))
            new_matrix.append(new_list)
        return new_matrix
# matrix = [[1, 2, 3], [4, 5, 6]]
# print(matrix_divided(matrix, "hello"))
# matrix = [[1, 2, 3], [4, 5, 6]]
# print(matrix_divided(matrix, "4"))
# matrix = [[1, 2, 3], [4, 5, 6]]
# print(matrix_divided(matrix, 0))
# matrix = [[1, 2, 3], [4, 5, 6], "3"]
# print(matrix_divided(matrix, 3))
# matrix = [[1, 2, 3], 20, [4, 5, 6]]
# print(matrix_divided(matrix, 3))
# matrix = [[1, 2, 3], ["4", None, 6], [4, 5, 6]]
# print(matrix_divided(matrix, 3))
# matrix = [[1, 2, 3], [1, 3, 4, 20], [4, 5, 6, 13]]
# print(matrix_divided(matrix, 3))
# x = float("inf")
# matrix = [[1, 2, 3], [4, 5, 6]]
# print(matrix_divided(matrix, x))
# matrix = [[1, 2, 3], [4, 5, 6]]
# print(matrix_divided(matrix))
# matrix = [[1, 2, 3], [4, 5, 6]]
# print(matrix_divided(3))
# matrix = [[1, 2, 3], [4, 5, 6]]
# print(matrix_divided())
