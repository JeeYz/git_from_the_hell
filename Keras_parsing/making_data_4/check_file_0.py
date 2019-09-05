# @Author: J.Y.
# @Date:   2019-09-05T12:40:37+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-09-05T17:44:51+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import time


# trainfile = 'd:/Program_Data/raw_train_dataset_25.train'
trainfile = 'd:/Program_Data/Parsing_Data_BiLSTM_batch/parsing_BiLSTM_batch_train_data_00.train'
# trainfile = 'd:/Program_Data/Parsing_Data_BiLSTM_batch/parsing_BiLSTM_batch_train_data_01.train'
# trainfile = 'd:/Program_Data/Parsing_Data_BiLSTM_batch/parsing_BiLSTM_batch_train_data_02.train'

with open(trainfile, 'r', encoding='utf-8') as fr:
    s_num = 0
    num = 0
    while True:
        line = fr.readline()
        if not line:break
        line = line.split()

        if line == []:
            if num != 41:
                print(num, '\t', s_num)
            num = 0
            s_num += 1
            continue

        num += 1

        # print(line)


















## endl
