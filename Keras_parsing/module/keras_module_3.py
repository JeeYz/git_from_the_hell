# @Author: J.Y.
# @Date:   2019-03-28T11:14:41+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-01T17:59:52+09:00
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

def generate_train_data3(fname):
    full_train_vectors = list()
    train_label = list()
    with open(fname, 'r', encoding='utf-8') as f:
        while True:
            word_vectors = list()
            pos_vectors = list()
            line = f.readline()
            if not line: break
            line = line.split()
            if line == []: continue
            num1 = 0
            for j in line[:-1]:
                if j == '##':
                    num1 += 1
                    continue
                if num1 < 18:
                    word_vectors.extend(words_matrix[int(j)])
                elif num1 < 36 and 18 <= num1:
                    train_vector.extend(pos_matrix[int(j)])
            full_train_vectors.append(train_vector)

            if int(line[-1]) == 0:
                train_label.append([1, 0, 0])
            elif int(line[-1]) == 1:
                train_label.append([0, 1, 0])
            elif int(line[-1]) == 2:
                train_label.append([0, 0, 1])
            num1 += 1

    return train_data, train_labels











## endl
