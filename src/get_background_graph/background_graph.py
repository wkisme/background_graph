def background_graph(list1):

    dic = {}
    for a in list1:
        dic.update(a)
    for k, v in dic.items():
        dic[k] = 0

    flag = 0
    for k1, v1 in dic.items():
        for a in list1:
            for k, v in a.items():
                if k == k1:
                    dic[k1] += a[k]
                else:
                    flag += 1
    return dic

# 把不同layer中的相同的边删除到只剩一个，并赋给权值
