# @Author: JY
# @Date:   2019-01-14T15:13:53+09:00
# @Filename: read_raw_data_01.py
# @Last modified by:   JY
# @Last modified time: 2019-01-15T11:46:49+09:00
# @Copyright: JeeY


import os

file_folder = 'd:/Programming/Corpus/HANTEC-2.0/DATA'

file_r_00 = 'data/data_result_00.txt'

file_list = []

if not os.path.isdir('data'):
    os.mkdir('./data')

for (path, dir, files)  in os.walk(file_folder):
    for filename in files:
        file_n = str(path) + '/' + str(filename)
        file_list.append(file_n)

# print(file_list)

with open(file_r_00, 'w', encoding='utf-8') as fw:
    for a_file in file_list:
        with open(a_file, 'r', encoding='utf-8') as f1:
            while True:
                line = f1.readline()
                print(line)
