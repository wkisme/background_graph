import pandas as pd
from src.excel_processing.file_path import file_path


def process_chapter():
    data = pd.read_excel(file_path + 'chapter.xlsx', sheet_name='chapter', usecols=[1, 2],
                         dtype=str, index_col=None, header=None)

    col1 = data[1]

    col2 = data[2]

    chapter = {}
    for i in range(len(col1)):
        if len(col1.iloc[i]) == 9:
            chapter['0'+col1.iloc[i][-1]] = col2.iloc[i]
        if len(col1.iloc[i]) == 10:
            chapter[col1.iloc[i][8]+col1.iloc[i][9]] = col2.iloc[i]
    return chapter


if __name__ == '__main__':
    process_chapter()
