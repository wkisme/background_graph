import pandas as pd
from src.excel_processing.file_path import file_path
import re


def process_heading():
    data = pd.read_excel(file_path + 'heading.xlsx', sheet_name='heading', usecols=[1, 2],
                         dtype=str, index_col=None, header=None)

    col1 = data[1]
    col2 = data[2]
    heading = {}

    for i in range(len(col1)):
        str1 = ''
        for j in re.findall(r'\d', col1.iloc[i]):

            str1 += j
        while len(str1) < 4:
            str1 += '0'

        heading[str1] = col2.iloc[i]

    return heading


if __name__ == '__main__':
    process_heading()
