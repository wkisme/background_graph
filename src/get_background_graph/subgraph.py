def subgraph(list1):
    dic = {}
    for a in list1:
        dic[a] = list1.count(a)
    return dic
