from src.similarity.same_elements import same_elements


def sim_deg(vertex1, matrix1, vertex2, matrix2):

    v1, v2, ultra_demomitor = same_elements(vertex1, vertex2)

    length = len(v1)
    # 求每个相同顶点的sim_deg

    l1 = []
    sum1 = 0
    for num in range(length):
        numerator = 0
        demomitor = 0
        l1.clear()
        # 每个顶点
        for i in range(length):
            if i != num:
                l1.append(matrix1[v1[i], v1[num]])

                l1.append(matrix2[v2[i], v2[num]])

                l1 = sorted(l1, reverse=False)  # 从小到大排序

                numerator += l1[0]  # 每个顶点的相似度，分子
                demomitor += l1[1]  # 分母
                l1.clear()
        row, column = matrix1.shape
        row2, colum2 = matrix2.shape
        for i in range(row):
            if i not in v1:

                demomitor += matrix1[i, v1[num]]
        for i in range(row2):

            if i not in v2:

                demomitor += matrix2[i, v2[num]]
        # print(numerator / demomitor)
        sum1 += numerator / demomitor

    return sum1/ultra_demomitor
