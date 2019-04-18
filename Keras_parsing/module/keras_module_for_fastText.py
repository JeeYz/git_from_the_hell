# @Author: J.Y.
# @Date:   2019-04-15T11:41:04+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-18T13:30:54+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import numpy as np
import random

np.random.seed(1)

# f_fastText_0 = 'D:/Program_Data/fastText/fastText-0.1.0/result/model_dim_128_skipgram_2.vec'
f_fastText_0 = 'D:/Program_Data/fastText/fastText-0.1.0/result/model_dim_128_skipgram_3.vec' ## No.3

f_fastText_1 = 'D:/Program_Data/fastText/fastText-0.2.0/result/pos_dim_128_skipgram_0.vec'

def words_matrix_fastText(wvec_size):
    w_matrix = list()
    temp = list()
    with open(f_fastText_0, 'r', encoding='utf') as f:
        switch = 0
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line[0] == '</s>':
                continue
            if line[0] == 'ROOT':
                c = line[1:]
                continue
            if switch == 0:
                switch = 1
            else:
                temp.append(line)
    temp.sort()
    for i in temp:
        # a = np.array(i[1:])
        # w_matrix.append(a)
        w_matrix.append(i[1:])
    # w_matrix.append(np.random.uniform(-1.0, 1.0, (wvec_size)))
    w_matrix.append(c) ## for fT No.3
    b = np.array(w_matrix)
    # w_matrix = b.astype('float32')
    return b

def make_pos_fastText(pvec_size):
    p_matrix = list()
    temp = list()
    with open(f_fastText_1, 'r', encoding='utf') as f:
        switch = 0
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line[0] == '</s>':
                continue
            if line[0] == 'ROOT':
                c = line[1:]
                continue
            if switch == 0:
                switch = 1
            else:
                temp.append(line)
    temp.sort()
    for i in temp:
        # a = np.array(i[1:])
        # w_matrix.append(a)
        p_matrix.append(i[1:])
    # w_matrix.append(np.random.uniform(-1.0, 1.0, (wvec_size)))
    p_matrix.insert(0, np.random.uniform(-1.0, 1.0, (pvec_size)))
    p_matrix.append(c) ## for fT No.3
    b = np.array(p_matrix)
    # w_matrix = b.astype('float32')
    return b












if __name__ == '__main__':
    print('hello, world~!')
    # p = make_pos_fastText(128)
    # for i in p:
    #     print(i)
    # print(len(p))


## endl
