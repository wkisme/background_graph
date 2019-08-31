
def calculate(matrix1, i, j):

    matrix = matrix1
    pass
    i_to = []
    row1, column1 = matrix.shape
    for row in range(row1):
        if row == i:
            for column in range(column1):
                if matrix[i, column] != 0 and i != column:
                    i_to.append(column)
    plus = []
    for row in i_to:
        for column in range(column1):
            if column == j and matrix[row, column] != 0:
                plus.append(matrix[i, row]*matrix[row, column])
    plus = sorted(plus, reverse=True)
    if len(plus):
        return plus[0]
    else:
        return 0


def degree2(matrix):

    matrix1 = matrix.copy()
    # print(matrix1)

    row, column = matrix.shape
    for i in range(row):
        for j in range(column):
            pass
            if matrix[i, j] == 0:

                matrix[i, j] = calculate(matrix1, i, j)
    print(matrix)
    return matrix

