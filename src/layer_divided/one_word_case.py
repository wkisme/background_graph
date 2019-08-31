def one_word_case(cn_subgraph):

    list1 = cn_subgraph.copy()

    dic1 = {}
    for i in range(len(list1)):
        dic1.clear()
        dic1 = list1[i].copy()
        # it's a shadow copy

        if len(dic1) == 1:

            if i == 0:
                for key, value in list1[i].items():
                    list1[i+1][key] = value
                del list1[i]

            if i != 0:
                for key, value in list1[i].items():
                    list1[i-1][key] = value
                del list1[i]
            break
    for i in range(len(list1)):
        dic1.clear()
        dic1 = list1[i].copy()

        if len(dic1) == 1:

            if i == 0:
                for key, value in list1[i].items():
                    list1[i+1][key] = value
                del list1[i]

            if i != 0:
                for key, value in list1[i].items():
                    list1[i-1][key] = value
                del list1[i]
            break
    return list1
