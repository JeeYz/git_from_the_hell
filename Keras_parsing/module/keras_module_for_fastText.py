# @Author: J.Y.
# @Date:   2019-04-15T11:41:04+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-15T14:15:20+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import numpy as np
import random

np.random.seed(1)

f_fastText_0 = 'D:/Program_Data/fastText/fastText-0.1.0/result/model_dim_128_skipgram_2.vec'

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
            if switch == 0:
                switch = 1
            else:
                temp.append(line)
    temp.sort()
    for i in temp:
        # a = np.array(i[1:])
        # w_matrix.append(a)
        w_matrix.append(i[1:])
    w_matrix.append(np.random.uniform(-1.0, 1.0, (wvec_size)))
    b = np.array(w_matrix)
    # w_matrix = b.astype('float32')
    return b

def pos_matrix_random(pvec_size):
    p_matrix = list()
    p_matrix = np.random.uniform(-1.0, 1.0, (pvec_size, pvec_size))
    return p_matrix

def make_pos_list(pvec_size):
    temp = list()
    pos_matrix = np.eye(pvec_size)
    return pos_matrix


if __name__ == '__main__':
    print('hello, world~!')

## endl
