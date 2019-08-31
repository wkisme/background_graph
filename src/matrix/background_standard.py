def background_standard(dic):

    l1 = []
    for k, v in dic.items():
        l4 = list(k)
        l1 = l1+l4
    l1 = set(l1)
    l1 = sorted(l1)
    list1 = []
    for key in dic.keys():
        list2 = [0, 0]
        pass
        b = 0
        for a in l1:
            if a == key[0]:
                list2[0] = b
            if a == key[1]:
                list2[1] = b
            b += 1
        list1 = list1+list2

        list2.clear()
    list_weight = []
    for value in dic.values():
        list_weight.append(value)

    return l1, list1, list_weight
