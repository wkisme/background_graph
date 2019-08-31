from src.test_excel.classification_number import classification_number


def f1_score_precision_positive(key, cn_us, each_cn_much_us1):
    list1 = sorted(each_cn_much_us1, key=each_cn_much_us1.__getitem__, reverse=True)

    if len(each_cn_much_us1) > classification_number:
        counter = 0
        for i in list1:

            if counter < classification_number:
                if i == cn_us[key]:
                    # TP=1
                    return 1
            counter += 1
            if counter == classification_number:
                break
        # FP=1
        return 2
    else:
        if len(each_cn_much_us1) == 0:
            return 5
        return 0
