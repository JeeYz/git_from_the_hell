# @Author: J.Y.
# @Date:   2019-04-29T10:17:13+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-27T14:07:45+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import os
import sys
import numpy as np
sys.path.append(r'../module')

import parsing_module_2 as p2

fname0 = 'd:/Program_Data/raw_test_dataset_06.test'
fname1 = 'd:/Program_Data/raw_test_dataset_07.test'

train_data = list()
word_dict = p2.making_dictionary_of_words()
pos_dict = p2.making_pos_dictionary()

with open(fname0, 'r', encoding='utf-8') as f:
    sent = list()
    while True:
        new = list()
        line = f.readline()
        if not line:break
        line = line.split()
        if line == []:
            train_data.append(sent)
            sent = list()
            continue
        new.append(line[0])
        new.append(str(word_dict[line[1]]))
        new.append(str(word_dict[line[3]]))
        new.append(str(pos_dict[line[2]]))
        new.append(str(pos_dict[line[4]]))
        sent.append(new)

# print(train_data[0])

with open(fname1, 'w', encoding='utf-8') as fw:
    for sent in train_data:
        for word in sent:
            fw.write('    '.join(word) + '\n')
        fw.write('\n')









## endl
