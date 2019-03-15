# @Author: J.Y.
# @Date:   2019-03-14T09:44:24+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-15T16:03:39+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import numpy as np

filepath = 'd:/Program_Data/'
file_word = 'result_raw_words_list_00.words'
file_pos = 'result_post_temp_01.pos'
file_arc = 'temp_result_09.temp'

np.random.seed(1)
wordvec_size = 128

def make_word_list(fname):
    temp = list()
    with open(fname, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            temp.append(line)
    words_matrix = np.random.uniform(-1.0, 1.0, (len(temp)+1, wordvec_size))
    return words_matrix

def make_pos_list(fname):
    temp = list()
    with open(fname, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            temp.append(line)
    pos_matrix = np.eye(len(temp)+1)
    return pos_matrix

def make_arc_list(fname):
    temp = list()
    with open(fname, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:break
            line = line.split()
            temp.append(line)
    arc_matrix = np.eye(len(temp)+1)
    return arc_matrix

def generate_train_data(filetuple, batch_size):
    words_matrix = make_word_list(filepath + file_word)
    pos_matrix = make_pos_list(filepath + file_pos)

    train_vector = list()
    train_label = list()

    for i in filetuple:
        with open(i, 'r', encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:break
                line = line.split()
                num1 = 0
                for j in line[:-1]:
                    if j == '##':
                        num1 += 1
                        continue
                    if num1 < 18:
                        pass

                    elif num1 < 36 and 18 <= num1:
                        pass

                train_label.append(line[-1])

    return (train_vector, train_label)






if __name__ == "__main__":
    print('hello, world~!')
    make_word_list(filepath + file_word)

## endl
