
from src.matrix.get_shape import getshape
import numpy as np


def pre_degree1(list_edge, list_weight, dic):
    shape = getshape(dic)
    a = np.zeros((shape, shape))

    a[0, 0] = 1

    flag = 0
    for abc in list_edge:
        if flag % 2 == 0:
            b = list_weight[flag//2]
            row = list_edge[flag]
            column = list_edge[flag + 1]
            a[row, column] = b
        flag += 1
    return a


def matrix_row_value(matrix, row):

    row1, column = matrix.shape
    sum1 = 0
    for i in range(row1):
        if i == row:
            for j in range(column):
                if i != j:
                    sum1 += matrix[i, j]

    return sum1


def degree1(matrix):

    matrix = bugfix_matrix_transpose(matrix)
    a = matrix.copy()   # it's a deep copy
    if a is matrix:
        print("you don't have a deep copy")

    row, column = a.shape

    for i in range(row):
        for j in range(column):
            if i != j:
                if a[i, j] != 0:
                    a[i, j] = matrix[i, j]/matrix_row_value(matrix, i)
    # print(np.around(a,decimals=2))
    return a


def bugfix_matrix_transpose(matrix):

    return matrix+matrix.transpose()
