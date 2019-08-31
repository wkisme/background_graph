
def background(list2):

    list1 = []
    dic1 = [{}, {}, {}]
    i = 0
    for dic in list2:
        dic2 = dic1[i]
        i = i+1
        for a in dic:
            for b in dic:
                if a < b:
                    c = dic[a] * dic[b]
                    d = (a, b)
                    dic2[d] = c
        list1.append(dic2)
    return list1

# 在同一个layer中，把两个vertex形成边，并赋给边权值。
# 并且对于(vertex1,vertex2),vertex1<vertex2


