# @Author: J.Y.
# @Date:   2019-05-09T11:29:24+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-28T10:51:24+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import time
import numpy as np

from keras.backend import argmax
from keras import backend as K

trainfile = 'd:/Program_Data/raw_train_dataset_23.train'
trainfile2 = 'd:/Program_Data/raw_train_dataset_24.train'
trainfile3 = 'd:/Program_Data/raw_test_dataset_09.test'

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

def make_train_data():
    word = list()
    pos = list()
    label = list()
    word_all = list()
    pos_all = list()
    label_all = list()
    with open(trainfile2, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []:
                # word = np.array([word])
                # pos = np.array([pos])
                # word_all.append([word])
                # pos_all.append([pos])
                word_all.append(word)
                pos_all.append(pos)
                new_label = list()
                for i in label:
                    new = list()
                    for j in range(len(label)):
                        if int(j) == int(i):
                            new.append(float(1))
                        else:
                            new.append(float(0))
                    new_label.append(new)
                # new_label = np.array(new_label)
                # label_all.append([new_label])
                label_all.append(new_label)
                word = list()
                pos = list()
                label = list()
                continue
            word.append([line[3], line[4]])
            pos.append([line[5], line[6]])
            label.append(line[1])
    # print(word_all)
    # time.sleep(100000)
    word_all = np.array(word_all)
    pos_all = np.array(pos_all)
    label_all = np.array(label_all)
    return word_all, pos_all, label_all


def make_test_data():
    word = list()
    pos = list()
    label = list()
    word_all = list()
    pos_all = list()
    label_all = list()
    with open(trainfile3, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []:
                # word = np.array([word])
                # pos = np.array([pos])
                # word_all.append([word])
                # pos_all.append([pos])
                word_all.append(word)
                pos_all.append(pos)
                new_label = list()
                for i in label:
                    new = list()
                    for j in range(len(label)):
                        if int(j) == int(i):
                            new.append(float(1))
                        else:
                            new.append(float(0))
                    new_label.append(new)
                # new_label = np.array(new_label)
                # label_all.append([new_label])
                label_all.append(new_label)
                word = list()
                pos = list()
                label = list()
                continue
            word.append([line[3], line[4]])
            pos.append([line[5], line[6]])
            label.append(line[1])
    # print(word_all)
    # time.sleep(100000)
    word_all = np.array(word_all)
    pos_all = np.array(pos_all)
    label_all = np.array(label_all)
    return word_all, pos_all, label_all


def evaluate_result(sys, label):
    new_sys = np.argmax(sys, axis=-1)
    new_label = np.argmax(label, axis=-1)
    print(new_sys)
    print(new_label)
    b = len(sys[0])
    a = 0
    for i, j in enumerate(new_sys[0]):
        if int(new_label[0][i]) == int(j):
            a += 1
    print(a, b)
    # time.sleep(10000)
    return a, b









if __name__ == '__main__':
    print('hello, world~!')

## endl
