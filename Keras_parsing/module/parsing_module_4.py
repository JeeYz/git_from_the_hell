# @Author: J.Y.
# @Date:   2019-05-28T10:46:18+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-09-05T16:20:47+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import time
import numpy as np

def make_train_data(trainfile):
    word = list()
    pos = list()
    label = list()
    word_all = list()
    pos_all = list()
    label_all = list()
    with open(trainfile, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []:
                word = np.array(word)
                pos = np.array(pos)
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

            # word.append([line[3], line[4]])
            # pos.append([line[5], line[6]])
            # label.append(line[1])

            word.append([line[3], line[4]])
            pos.append([line[5], line[6]])
            label.append(line[1])

    # print(word_all)
    # time.sleep(100000)
    word_all = np.array(word_all)
    pos_all = np.array(pos_all)
    label_all = np.array(label_all)
    # print(word_all.shape)
    # print(word_all[0])
    return word_all, pos_all, label_all



if __name__ == '__main__':
    print('hello, world~!')













## endl
