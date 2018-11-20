# @Author: JayY
# @Date:   2018-09-08T09:15:50+09:00
# @Filename: new_24.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-19T16:26:45+09:00
# @Copyright: JayY

# new_24.py
# practice for skipgram
# this file is not complete skipgram
# practice and prototype
# ===================================================

'''
mini skip gram model
prototype
not complete version
'''

import collections
import numpy as np
import random
import tensorflow as tf
import sys
sys.setrecursionlimit(50000)

f_read1 = open("result_03.txt", 'r', encoding='utf-8')
f_read2 = open("result_04.txt", 'r', encoding='utf-8')
fp = open('result_sent_01.txt', 'r', encoding='utf-8')

fpr = open('train_skip_01.txt', 'r', encoding='utf-8')
fpw = open('train_skip_01_result.txt', 'w', encoding='utf-8')

data_index = 0

batch_size = 10
learning_rate = 0.01
input_size = 300
window_size = 2
skip_num = window_size*2
num_skip = skip_num + 1

def make_dict_data():
    dict_word = dict()
    dict_node = dict()
    word_mtx = list()
    node_mtx = list()
    while True:
        line = f_read1.readline().split()
        if not line : break
        dict_word[line[0]] = list()
        for i in range(input_size):
            word_mtx.append(line[i+4])
        dict_word[line[0]].append(line[1])
        dict_word[line[0]].append(line[304:])
    while True:
        line = f_read2.readline().split()
        if not line: break
        dict_node[line[0]] = list()
        for i in range(input_size):
            node_mtx.append(line[i+4])
        dict_node[line[0]].append(line[1])
        dict_node[line[0]].append(line[304:])

    word_mtx = np.array(word_mtx)
    word_mtx = word_mtx.reshape(-1, 300)
    node_mtx = np.array(node_mtx)
    node_mtx = word_mtx.reshape(-1, 300)

    num_word = len(dict_word)
    num_node = len(dict_node)
    ### making dummy word
    a = list()
    for i in range(window_size*2):
        b = np.random.uniform(-1.0, 1.0, 300)
        a.append(b)
        c = 'dummy_00'+str(i)
        dict_node[c] = list()
        dict_node[c].append(num_node + i)
        dict_node[c].append(list())
    dummy = np.array(a).reshape(-1, 300)
    print(dummy, type(dummy), dummy.shape)
    node_mtx = np.concatenate((node_mtx, dummy)) #더미를 뒤에 붙임
    print(node_mtx, type(node_mtx), node_mtx.shape)
    #print(dict_word, type(dict_word))
    return word_mtx, node_mtx, dict_word, dict_node

word_mtx, node_mtx, dict_word, dict_node = make_dict_data()

def make_train_file(dict_node, dict_word):
    while True:
        line = fpr.readline()
        if not line: break
        line = line.split()
        line_t = list(line)
        for i in reversed(range(window_size)):
            t = 'dummy_00' + str(i)
            line_t.insert(0, t)
        for i in range(window_size, 2*window_size):
            t = 'dummy_00' + str(i)
            line_t.append(t)
        print(len(line), len(line_t))
        for i in range(len(line)):
            for j in range(num_skip):
                if j==window_size: continue
                a = dict_word.get(line[i])[0]
                if 'dummy_0' in line_t[j+i]:
                    b = dict_node.get(line_t[j+i])[0]
                    a, b = str(a), str(b)
                    fpw.write(a + '\t' + b + '\n')
                else:
                    l = dict_word.get(line_t[j+i])[1]
                    #print(type(l)
                    a = str(a)
                    fpw.write(a + '\t' + '0' + '\n') # huff_root
                    m = list()
                    for k in l:
                        m.append(k)
                        for v in dict_node.values():
                            if v[1] == m:
                                b = str(v[0])
                                fpw.write(a + '\t' + b + '\n')

make_train_file(dict_node, dict_word)

X_word = tf.placeholder(tf.int32, shape=[batch_size], name='X_value_from_word_vector')
X_node = tf.placeholder(tf.int32, shape=[batch_size], name='X_value_from_node_vector')
Y = tf.placeholder(tf.int32, shape=[batch_size, 1], name='Y_label_value')

X_input1 = tf.Variable(word_mtx, dtype=tf.float32, name='X_data_for_word_vector')
X_input2 = tf.Variable(node_mtx, dtype=tf.float32, name='X_data_for_node_vector')
W_weight = tf.Variable(tf.random_uniform([600, 1], -1.0, 1.0, seed=1),
                       dtype=tf.float32, name='weight_matrix')
'''
res = tf.sigmoid(tf.matmul(X_input1, X_node))
cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=Y, logits=res))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

init = tf.global_variables_initializer()
with tf.Session() as session:
    session.run(init)

    for _ in range(batch_size):
        pass
'''
