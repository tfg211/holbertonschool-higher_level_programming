#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    It computes the square value of all integers of a matrix using map().
    """
    # 1st. define the squaring operation (lambda function)
    # The lambda function takes x and returns x squared (x**2).
    # 2nd. Uses map() on the outer list (matrix)
    # The outer map applies an operation to *each row* in the matrix.
    # The operation is: 'Take a row, and >>
    # >> map the squaring function onto every item in that row.'
    # list() converts the map object back into a list.
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
