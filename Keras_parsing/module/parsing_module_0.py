# @Author: J.Y.
# @Date:   2019-04-05T10:27:57+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-08T17:20:08+09:00
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

class tree_node():
    def __init__(self):
        self.index = None
        self.dependency = None
        self.word = None

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
    with open(filename1, 'r', encoding='utf-8') as f:
        switch = 1
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if switch == 1:
                all_sents.append(line)
                switch = 0
                continue
            if line == []:
                switch = 1
    return all_sents

def make_stack_buffer_list(sent):
    stack = list(sent[:2])
    buffer = list(sent[2:])
    return stack, buffer

def generate_data_of_test():
    # stack && buffer
    # tree
    # sentence
    # parsing table

    with open(filename1, 'r', encoding='utf-8') as f1:
        while True:
            line = f1.readline()
            if not line:break
            line = line.split()

    return









if __name__ == '__main__':
    print('hello, world~!~!')

## endl
