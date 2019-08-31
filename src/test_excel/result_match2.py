def result_match2(key, cn_us, each_cn_much_us1):
    list1 = sorted(each_cn_much_us1, key=each_cn_much_us1.__getitem__, reverse=True)

    # 模糊匹配
    if len(each_cn_much_us1) > 0:
        w = 1/len(list1)

        counter = 0
        for i in list1:
            if i == cn_us[key]:

                return 1-counter*w
            counter += 1

        print('不存在期望的hscode',key)
        return 2
    else:
        # print('对应的列表为空', key)
        return 0

