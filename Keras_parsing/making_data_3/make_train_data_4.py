# @Author: J.Y.
# @Date:   2019-05-22T11:18:51+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-22T14:25:01+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

trainfile1 = 'd:/Program_Data/raw_train_dataset_05.train'
trainfile2 = 'd:/Program_Data/raw_train_dataset_22.train'
trainfile3 = 'd:/Program_Data/raw_train_dataset_24.train'

import os
import numpy as np

with open(trainfile1, 'r', encoding='utf-8') as fr1,\
open(trainfile2, 'r', encoding='utf-8') as fr2,\
open(trainfile3, 'a', encoding='utf-8') as fw:
    one_word = list()
    switch = 1
    while True:
        line1 = fr1.readline()
        line2 = fr2.readline()
        if not line1:break
        line1 = line1.split()
        line2 = line2.split()
        if line1 == []:
            switch = 1
            fw.write('\n')
            one_word = list()
            continue
        if switch == 1:
            one_word.append(str(0))
            one_word.append(str(0))
            one_word.extend(line2)
            switch = 0
            fw.write('   '.join(one_word) + '\n')
            one_word = list()
            continue

        one_word.append(line1[0])
        one_word.append(line1[1])
        one_word.extend(line2)
        fw.write('   '.join(one_word) + '\n')
        one_word = list()















## endl
