# Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. 
# The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.

import numpy as np

def transpose(matrix):
    n_rows = len(matrix)
    n_columns = len(matrix[0])

    transposed = np.zeros((n_columns, n_rows))

    for i in range(n_rows):
        for j in range(n_columns):
            transposed[j][i] = matrix[i][j]

    print(transposed)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)

'''
Example Output:

[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
[
    [1, 4],
    [2, 5],
    [3, 6]
]
'''