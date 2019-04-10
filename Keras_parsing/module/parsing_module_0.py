# @Author: J.Y.
# @Date:   2019-04-05T10:27:57+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-11T08:11:04+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import numpy as np

import keras_module_0 as k0
import keras_module_1 as k1
import keras_module_2 as k2

fpath1 = 'd:/Program_Data/'
filename1 = fpath1 + 'raw_test_dataset_01.test'
filename2 = fpath1 + 'raw_test_dataset_05.test'
filename3 = fpath1 + 'result_raw_words_list_00.words'
filename4 = fpath1 + 'result_pos_temp_01.pos'

class tree_node:
    def __init__(self, i, w):
        self.index = int(i)
        self.word = w
        self.children = list()
        self.depend = None

def make_dependency_tree(sent):
    action_stack = list()
    for i,j in enumerate(sent, 1):
        new = tree_node(i, j)
        action_stack.append(new)
    return action_stack

def make_all_init_test_data():
    data = list()
    with open(filename2, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []:
                continue
            new = list()
            word = list()
            pos = list()
            num = 0
            for i in line:
                if i == '##':
                    num += 1
                    continue
                if num < 18:
                    word.append(i)
                elif num >= 18:
                    pos.append(i)
            new.append([word])
            new.append([pos])
            data.append(new)
    data = np.array(data)
    return data

def make_all_sents_to_list():
    all_sents = list()
    words_data = list()
    with open(filename1, 'r', encoding='utf-8') as f:
        switch = 1
        one_sent = list()
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if switch == 1:
                all_sents.append(line)
                switch = 0
                continue
            if line == []:
                words_data.append(one_sent)
                one_sent = list()
                switch = 1
                continue
            one_sent.append(line)
    return all_sents, words_data

def make_stack_buffer_list(sent):
    stack = list()
    stack.insert(0, 'ROOT')
    stack.insert(0, sent[0])
    stack.insert(0, sent[1])
    buffer = list(sent[2:])
    return stack, buffer

def make_words_pos_dict():
    words = dict()
    pos = dict()
    words['NULL'] = 0
    pos['NULL'] = 0
    num = 1
    with open(filename3, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            words[line[0]] = num
            num += 1
    num = 1
    with open(filename4, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            pos[line[1]] = num
            num += 1
    return words, pos

def select_action(init_result):
    if init_result[0][0] > init_result[0][1] and init_result[0][0] > init_result[0][2]:
        act = 'shift'
    elif init_result[0][1] > init_result[0][0] and init_result[0][1] > init_result[0][2]:
        act = 'left'
    else:
        act = 'right'
    return act





if __name__ == '__main__':
    print('hello, world~!~!')

## endl
