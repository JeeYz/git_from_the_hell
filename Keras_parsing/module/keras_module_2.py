# @Author: J.Y.
# @Date:   2019-03-27T11:28:24+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-28T09:48:48+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

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

def make_stack_buffer_list():
    stack, buffer = list(), list()
    with open(filename1, 'r', encoding='utf-8') as f:
        switch = 1
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []:
                switch = 1
                continue
            if switch == 1:
                a = list(line[:2])
                b = list(line[2:])
                stack.append(a)
                buffer.append(b)
                switch = 0
                continue
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
    print('hello, world~!')

## endl
