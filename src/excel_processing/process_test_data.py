import pandas as pd
from src.excel_processing.file_path import file_path


def process_test_data():

    data = pd.read_excel(file_path+'test_data.xlsx', sheet_name=0, usecols=[2, 3], dtype=str)

    col1 = data['Expected HS code (from USA 2019)']
    col2 = data['Expected HS code (from China 1.1xlsx)']

    source_hscode = {}
    for i in range(len(col2)):
        if i > 0:
            if type(col2.iloc[i]) != float:
                if type(col1.iloc[i]) != float:
                    source_hscode[col2.iloc[i]] = col1.iloc[i]
    return source_hscode


if __name__ == '__main__':
    process_test_data()
