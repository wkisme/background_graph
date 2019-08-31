from src.excel_processing.process_test_data import process_test_data
from src.excel_processing.process_test_data_2 import process_test_data_2
from src.excel_processing.process_chapter import process_chapter
from src.excel_processing.process_heading import process_heading
from src.excel_processing.process_detail import process_detail
from src.excel_processing.process_us_data import process_us_data
import pickle
from src.pickle.pickle_file_path import pickle_file_path

if __name__ == '__main__':
    cn_us_2 = process_test_data_2()
    pickle.dump(cn_us_2, open(pickle_file_path + "cn_us_2.p", "wb"))


'''cn_us = process_test_data()
    pickle.dump(cn_us, open(pickle_file_path+"cn_us.p", "wb"))

    cn_us_2 = process_test_data_2()
    pickle.dump(cn_us_2, open(pickle_file_path + "cn_us_2.p", "wb"))

    chapter = process_chapter()
    pickle.dump(chapter, open(pickle_file_path+"chapter.p", "wb"))

    heading = process_heading()
    pickle.dump(heading, open(pickle_file_path+"heading.p", "wb"))

    detail = process_detail()
    pickle.dump(detail, open(pickle_file_path+"detail.p", "wb"))

    us_data = process_us_data()
    pickle.dump(us_data, open(pickle_file_path+"us_data.p", "wb"))
'''

