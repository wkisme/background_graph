
from src.test_excel.each_cn_much_us import each_cn_much_us
from src.test_excel.f1_score_precision_positive import f1_score_precision_positive
from src.test_excel.f1_score_precision_negative import f1_score_precision_negative
import pickle
from src.pickle.pickle_file_path import pickle_file_path

cn_us = pickle.load(open(pickle_file_path+"cn_us.p", "rb"))
chapter = pickle.load(open(pickle_file_path+"chapter.p", "rb"))
heading = pickle.load(open(pickle_file_path+"heading.p", "rb"))
detail = pickle.load(open(pickle_file_path+"detail.p", "rb"))
us_data = pickle.load(open(pickle_file_path+"us_data.p", "rb"))

if __name__ == '__main__':
    each_cn_much_us1 = {}
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    counter = 0
    no_exist = 0

    for key in cn_us.keys():
        # if key == '0504001400':

            each_cn_much_us1.clear()
            each_cn_much_us1 = each_cn_much_us(key, chapter, heading, detail, us_data)
            result = f1_score_precision_positive(key, cn_us, each_cn_much_us1)

            if result == 1:
                TP += 1
            if result == 2:
                FP += 1
            if result == 3:
                TN += 1
            if result == 4:
                FN += 1
            result = f1_score_precision_negative(key, cn_us, each_cn_much_us1)
            # print(result)
            if result == 1:
                TP += 1
            if result == 2:
                FP += 1
            if result == 3:
                TN += 1
            if result == 4:
                FN += 1
            if result == 0:
                counter += 1
            if result == 5:
                no_exist += 1

    print(TP, FP, TN, FN)
    precision = TP/(TP+FP)
    print('precision: ', precision)
    recall = TP/(TP+FN)
    print('召回率：', recall)
    f1 = 2*precision*recall/(precision+recall)
    print('F1_score: ', f1)
    print('候选个数少于3个的数目: ', counter)
    print("空表个数: ", no_exist)


