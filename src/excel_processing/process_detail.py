import pandas as pd
from src.excel_processing.file_path import file_path
import re


def process_detail():

    data = pd.read_excel(file_path + 'detail.xlsx', sheet_name='detail', usecols=[1, 2],
                         dtype=str, index_col=None, header=None)

    col1 = data[1]

    col2 = data[2]

    detail = {}
    for i in range(len(col1)):
        str1 = ''
        for j in re.findall(r'\d', col1.iloc[i]):
            str1 += j
        while len(str1) < 10:
            str1 += '0'
        detail[str1] = col2.iloc[i]

    return detail


if __name__ == '__main__':
    process_detail()
