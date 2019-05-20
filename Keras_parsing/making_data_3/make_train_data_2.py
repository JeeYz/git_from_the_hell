# @Author: J.Y.
# @Date:   2019-05-03T11:51:59+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-20T16:18:58+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import os
import sys
import numpy as np
sys.path.append(r'../module')

import parsing_module_2 as p2

fname1 = 'd:/Program_Data/raw_train_dataset_21.train'
fname2 = 'd:/Program_Data/raw_train_dataset_22.train'

train_data = list()
word_dict = p2.making_dictionary_of_words()
pos_dict = p2.making_pos_dictionary()

# print(word_dict)

with open(fname1, 'r', encoding='utf-8') as f, open(fname2, 'a', encoding='utf-8') as fw:
    switch = 1
    sent = list()
    while True:
        if switch == 1:
            new = list()
            new.append('ROOT')
            new.append(str(word_dict['ROOT']))
            new.append(str(word_dict['ROOT']))
            new.append(str(pos_dict['ROOT']))
            new.append(str(pos_dict['ROOT']))
            fw.write('    '.join(new) + '\n')
            switch = 0
            continue
        new = list()
        line = f.readline()
        if not line:break
        line = line.split()
        if line == []:
            switch = 1
            fw.write('\n')
            continue
        # print(line)
        new.append(line[0])
        new.append(str(line[1]))
        new.append(str(line[2]))
        new.append(str(line[3]))
        new.append(str(line[4]))
        fw.write('    '.join(new) + '\n')










## endl
