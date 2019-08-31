import pandas as pd
from src.excel_processing.file_path import file_path
import re


def flat(before_i, counter, str1, indent, col1, col3, source_description):
    flag1 = 0
    flag2 = 0
    for i in range(before_i, counter):
        str2 = ''
        if type(col1.iloc[i]) == float:
            pass
        else:
            for j in re.findall(r'\d', col1.iloc[i]):
                str2 += j

        if (len(str2) == 6) & (len(str1) > len(str2)):

            if str1[0] == str2[0]:
                if str1[1] == str2[1]:
                    if str1[2] == str2[2]:
                        if str1[3] == str2[3]:

                            if str1[4] == str2[4]:
                                if str1[5] == str2[5]:
                                    source_description += ' '
                                    source_description += col3.iloc[i]
                                    flag1 = 1
        if (len(str2) == 8) & (len(str1) > len(str2)):
            if str1[0] == str2[0]:
                if str1[1] == str2[1]:
                    if str1[2] == str2[2]:
                        if str1[3] == str2[3]:

                            if str1[4] == str2[4]:
                                if str1[5] == str2[5]:

                                    if str1[6] == str2[6]:
                                        if str1[7] == str2[7]:
                                            flag2 = 1
                                            source_description += ' '
                                            source_description += col3.iloc[i]
        if (indent == 2) & (flag1 == 1):
            break
        if flag2 == 1:
            break

    return source_description


def process_us_data():
    data = pd.read_excel(file_path + 'us_data.xls', sheet_name=0, usecols='A,B,C',
                         dtype=str, index_col=None, header=0)

    col1 = data['HTS Number']
    col2 = data['Indent']
    col3 = data['Description']
    us_data = {}

    before_i = 0
    before_str1 = '    '
    for i in range(len(col1)):
        flag = 0
        str1 = ''
        # 判断是否是nan
        if type(col1.iloc[i]) == float:
            pass
        else:
            for j in re.findall(r'\d', col1.iloc[i]):
                str1 += j
            if len(str1) > 4:
                if str1[0] == before_str1[0]:
                    if str1[0] == before_str1[0]:
                        if str1[0] == before_str1[0]:
                            if str1[0] == before_str1[0]:
                                flag = 1
            else:
                flag = 0
            if flag == 0:
                before_str1 = str1
                before_i = i
            if type(col2.iloc[i]) != float:
                if int(col2.iloc[i]) > 1:
                    col3.iloc[i] = flat(before_i, i, str1, col2.iloc[i], col1, col3, col3.iloc[i])

            us_data[str1] = col3.iloc[i]
    return us_data
