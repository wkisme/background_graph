
def same_elements(list1, list2):
    # 此处传入的list不含重复元素，且其中元素是经过排序的

    pass
    a = 0
    b = 0
    # l1=l2=[]  THIS IS WRONG!!!!!!!!
    l1 = []
    l2 = []

    for i in list1:
        for j in list2:
            if i == j:
                l1.append(a)
        a += 1
    for i in list2:
        for j in list1:
            if i == j:
                l2.append(b)
        b += 1

    a_set = set(list1)
    b_set = set(list2)
    c_set = a_set | b_set

    # 找到两个集合中不同的顶点
    ultra_demomitor = len(c_set)

    return l1, l2, ultra_demomitor
# 此处的v1,v2返回相同元素对应在不同矩阵的下标
