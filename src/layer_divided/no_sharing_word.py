def no_sharing_word(cn_subgraph):
    list1 = cn_subgraph.copy()
    sharing_flag = 0
    dic = {}
    for i in range(len(list1)):
        dic.clear()
        sharing_flag = 0
        dic = list1[i].copy()
        for key in dic.keys():

            for j in range(len(list1)):
                if i != j:
                    for key1 in list1[j].keys():
                        if key == key1:
                            sharing_flag = 1
        if sharing_flag == 0 & len(list1) > 1:
            if i == 0:
                for key, value in list1[i].items():
                    list1[i + 1][key] = value
                del list1[i]
            if i != 0:
                for key, value in list1[i].items():
                    list1[i - 1][key] = value
                del list1[i]
        break

    for i in range(len(list1)):
        dic.clear()
        sharing_flag = 0
        pass

        dic = list1[i].copy()

        for key in dic.keys():

            for j in range(len(list1)):
                if i != j:
                    for key1 in list1[j].keys():
                        if key == key1:
                            sharing_flag = 1
        if sharing_flag == 0 & len(list1) > 1:
            if i == 0:
                for key, value in list1[i].items():
                    list1[i + 1][key] = value
                del list1[i]
            if i != 0:
                for key, value in list1[i].items():
                    list1[i - 1][key] = value
                del list1[i]
        break

    return list1
