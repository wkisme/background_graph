def getshape(dic):
    l1 = []
    for k, v in dic.items():
        l4 = list(k)
        l1 = l1+l4
    l1 = set(l1)
    return len(l1)
