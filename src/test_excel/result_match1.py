def result_match1(key, cn_us, each_cn_much_us1):
    list1 = sorted(each_cn_much_us1, key=each_cn_much_us1.__getitem__, reverse=True)
    # 输出排序过后的相似度
    # 精确匹配 # noqa
    if len(each_cn_much_us1) > 0:
        if list1[0] == cn_us[key]:
            return 1
        if cn_us[key] in list1:
            pass
        else:
            print(key)
            return 2
    return 0
