# @Author: J.Y.
# @Date:   2019-03-28T11:14:41+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-01T11:55:30+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import numpy as np

filepath = 'd:/Program_Data/'
file_word = filepath + 'result_raw_words_list_00.words'
file_pos = filepath + 'result_pos_temp_01.pos'

np.random.seed(1)
WORDVEC_SIZE = 128

def make_word_list():
    temp = list()
    with open(file_word, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            temp.append(line)
    words_matrix = np.random.uniform(-1.0, 1.0, (len(temp)+1, WORDVEC_SIZE))
    return words_matrix

def make_pos_list():
    temp = list()
    with open(file_pos, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            temp.append(line)
    pos_matrix = np.eye(len(temp)+1)
    return pos_matrix













## endl
