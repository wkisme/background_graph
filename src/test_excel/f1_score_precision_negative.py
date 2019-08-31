from src.test_excel.classification_number import classification_number


def f1_score_precision_negative(key, cn_us, each_cn_much_us1):
    list1 = sorted(each_cn_much_us1, key=each_cn_much_us1.__getitem__, reverse=True)

    if len(each_cn_much_us1) > classification_number:
        counter = 0
        for i in list1:

            if counter >= classification_number:
                if i == cn_us[key]:
                    # TN = 1
                    return 3
            counter += 1

        # FN = 1
        return 4
    else:
        if len(each_cn_much_us1) == 0:
            return 5

        # print('对应的列表长度小于3', key)
        return 0
