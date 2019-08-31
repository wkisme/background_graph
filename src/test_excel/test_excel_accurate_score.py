
from src.test_excel.each_cn_much_us import each_cn_much_us
from src.test_excel.result_match1 import result_match1
import pickle
from src.pickle.pickle_file_path import pickle_file_path

cn_us = pickle.load(open(pickle_file_path+"cn_us.p", "rb"))
chapter = pickle.load(open(pickle_file_path+"chapter.p", "rb"))
heading = pickle.load(open(pickle_file_path+"heading.p", "rb"))
detail = pickle.load(open(pickle_file_path+"detail.p", "rb"))
us_data = pickle.load(open(pickle_file_path+"us_data.p", "rb"))


if __name__ == '__main__':
    each_cn_much_us1 = {}
    result = 0
    counter = 0
    no_exist = 0
    for key in cn_us.keys():
        # if key == '0201100010':

            each_cn_much_us1.clear()
            each_cn_much_us1 = each_cn_much_us(key, chapter, heading, detail, us_data)
            result = result_match1(key, cn_us, each_cn_much_us1)

            if result == 2:
                no_exist += 1
            else:
                counter += result

    print(counter)
    print(len(cn_us))
    print(counter/len(cn_us))
    print(no_exist)











