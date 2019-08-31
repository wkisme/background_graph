
def processing_diagonal(matrix):

    row, column = matrix.shape
    for i in range(row):
        for j in range(column):
            if i == j:
                matrix[i, j] = 1

    return matrix
