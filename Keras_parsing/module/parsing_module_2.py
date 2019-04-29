# @Author: J.Y.
# @Date:   2019-04-25T11:43:51+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-29T15:12:20+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import numpy as np

file1 = 'd:/Program_Data/result_raw_words_list_00.words'
file2 = 'd:/Program_Data/result_pos_temp_01.pos'
trainfile = 'd:/Program_Data/raw_train_dataset_21.train'
trainfile1 = 'd:/Program_Data/raw_train_dataset_05.train'

def make_matrix_A(a):
    return

def make_matrix_B(b):
    return

def making_dictionary_of_words():
    words_dict = dict()
    with open(file1, 'r', encoding='utf-8') as f:
        index_num = 1
        words_dict['NULL'] = 0
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            words_dict[line[0]] = index_num
            index_num += 1
    return words_dict

def making_pos_dictionary():
    pos_dict = dict()
    with open(file2, 'r', encoding='utf-8') as f:
        index_num = 1
        pos_dict['NULL'] = 0
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            pos_dict[line[1]] = index_num
            index_num += 1
    return pos_dict

def make_all_data():
    all_word, all_pos = list(), list()
    with open(trainfile, 'r', encoding='utf-8') as f:
        sent_word = list()
        sent_pos = list()
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []:
                all_word.append(sent_word)
                all_pos.append(sent_pos)
                sent_word = list()
                sent_pos = list()
                continue
            new_word = list()
            new_pos = list()
            new_word.append(line[1])
            new_word.append(line[2])
            new_pos.append(line[3])
            new_pos.append(line[4])
            sent_word.append(new_word)
            sent_pos.append(new_pos)

    return all_word, all_pos

def make_label_matrix()
    all_label = list()
    with open(trainfile1, 'r', encoding='utf-8') as f:
        switch = 1
        sent = list()
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []:
                all_label.append(sent)
                sent = list()
                switch = 1
                continue
            if switch == 1:
                len = len(line)
                switch = 0
                continue
            word_list = make_one_word_list(int(line[1]), len)
            sent.append(word_list)
    return all_label

def make_one_word_list(num, len):
    new = list()
    if i in range(len):
        if i == num:
            new.append(1)
        else:
            new.append(0)
    return new

def make_softmax(matrix):
    result = list()
    for i in matrix:
        line = list()
        sum  = 0
        for j in i:
            sum += np.exp(j)
        for j in i:
            line.append(np.exp(j)/sum)
        result.append(line)
    return result








## endl
