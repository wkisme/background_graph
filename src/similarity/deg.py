
def deg(index, matrix):
    sum1 = 0
    row, column = matrix.shape
    for i in range(row):
        for j in range(column):
            if j == index and i != j:
                sum1 += matrix[i, j]
    return sum1
