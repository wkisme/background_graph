import pandas as pd
from src.excel_processing.file_path import file_path
import re

def process_test_data_2():

    data = pd.read_excel(file_path+'test_data_2.xlsx', sheet_name=1, usecols=[2, 3], dtype=str)

    col1 = data['Expected HS code (from USA 2019)']
    col2 = data['Expected HS code (from China 1.1xlsx)']

    source_hscode = {}
    for i in range(len(col2)):
        if i > 0:
            if type(col2.iloc[i]) != float:
                if type(col1.iloc[i]) != float:
                    str1 = ''
                    str2 = ''
                    for j in re.findall(r'\d', col2.iloc[i]):
                        str2 += j
                    for j in re.findall(r'\d', col1.iloc[i]):
                        str1 += j
                    source_hscode[str2] = str1

    return source_hscode


if __name__ == '__main__':
    process_test_data_2()
