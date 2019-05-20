# @Author: J.Y.
# @Date:   2019-05-09T11:29:24+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-20T16:26:59+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import numpy as np
from keras.backend import argmax
from keras import backend as K

trainfile = 'd:/Program_Data/raw_train_dataset_23.train'

def make_small_train_data():
    word = list()
    pos = list()
    label = list()
    sent_w = list()
    sent_p = list()
    with open(trainfile, 'r', encoding='utf-8') as f:
        switch = 1
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []:
                switch = 2
                continue
            if switch == 2:
                label.append(line[1])
                continue
            word.append([line[1], line[2]])
            pos.append([line[3], line[4]])
    # print(word, '\n\n')
    # print(pos, '\n\n')
    # label = np.array(label)
    label.insert(0, 0)
    # print(label, '\n\n')

    word = np.array([word])
    pos = np.array([pos])
    new_label = list()
    for i in label:
        new = list()
        for j in range(len(label)):
            if int(j) == int(i):
                new.append(float(1))
            else:
                new.append(float(0))
        new_label.append(new)
    new_label = np.array([new_label])
    return word, pos, new_label

def find_argmax(x):
    return K.argmax(x, axis=-1)





if __name__ == '__main__':
    print('hello, world~!')

## endl
