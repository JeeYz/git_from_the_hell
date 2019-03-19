# @Author: J.Y.
# @Date:   2019-03-14T09:44:24+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-19T16:06:57+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import numpy as np

filepath = 'd:/Program_Data/'
file_word = 'result_raw_words_list_00.words'
file_pos = 'result_pos_temp_01.pos'
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

def generate_train_data(filename):
    words_matrix = make_word_list(filepath + file_word)
    pos_matrix = make_pos_list(filepath + file_pos)

    full_train_vectors = list()
    train_label = list()
    with open(filename, 'r', encoding='utf-8') as f:
        num1 = 0
        while True:
            train_vector = list()
            line = f.readline()
            if not line:break
            line = line.split()
            if line == []:continue
            num1 = 0
            for j in line[:-1]:
                if j == '##':
                    num1 += 1
                    continue
                if num1 < 18:
                    train_vector.append(list(words_matrix[int(j)]))
                elif num1 < 36 and 18 <= num1:
                    train_vector.append(list(pos_matrix[int(j)]))

            full_train_vectors.append(train_vector)

            if int(line[-1]) == 0:
                train_label.append([1, 0, 0])
            elif int(line[-1]) == 1:
                train_label.append([0, 1, 0])
            elif int(line[-1]) == 2:
                train_label.append([0, 0, 1])
            num1 += 1
    print('data load complete!!')
    full_train_vectors = np.array(full_train_vectors)
    train_label = np.array(train_label)
    return full_train_vectors, train_label, num1

def divide_train_data(x_data, y_data, num, batch_size, max):
    x_list, y_list = list(), list()
    if batch_size*(num+1) <= max:
        for i in range(num*batch_size, batch_size*(num+1)):
            x_list.append(x_data[i])
            y_list.append(y_data[i])
    else:
        for i in range(num*batch_size, max):
            x_list.append(x_data[i])
            y_list.append(y_data[i])
    return x_list, y_list



if __name__ == "__main__":
    print('hello, world~!')
    make_word_list(filepath + file_word)

## endl
