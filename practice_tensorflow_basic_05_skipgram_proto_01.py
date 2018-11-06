# @Author: JayY
# @Date:   2018-10-05T16:16:18+09:00
# @Filename: new_35.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:41:32+09:00
# @Copyright: JayY

# new_35.py
# skipgram prototype
# this file is not a complete skipgram file
# ===================================================

'''
skip gram ver1.0.0
not complete version
'''

import collections
import tensorflow as tf
import numpy as np
import random
import copy
import sys
sys.setrecursionlimit(50000)

fp_gb = open('train_skip_01_result.txt', 'r', encoding='utf-8')

batch_size = 10
epoch = 1
lrate = 0.0001

def build_dataset():
    with open("result_03.txt", 'r', encoding='utf-8') as f:
        word_mtx = list()
        while True:
            line = f.readline().split()
            if not line: break
            a = list(line[4:304])
            word_mtx += a
    with open("result_04.txt", 'r', encoding='utf-8') as f:
        node_mtx = list()
        while True:
            line = f.readline().split()
            if not line: break
            a = list(line[4:304])
            node_mtx += a
    word_mtx = np.array(word_mtx).reshape(-1, 300)
    node_mtx = np.array(node_mtx).reshape(-1, 300)
    print(type(word_mtx), word_mtx.shape)
    print(type(node_mtx), node_mtx.shape)
    return word_mtx, node_mtx

word_mtx, node_mtx = build_dataset()

def generate_batch(fp):
    input1, input2, label = list(), list(), list()
    for i in range(batch_size):
        line = fp.readline().split()
        if not line: break
        input1.append(int(line[0]))
        input2.append(int(line[1]))
        label.append(line[2])
    return input1, input2, label

X_word = tf.placeholder(tf.int32, shape=[batch_size], name='X_from_word_matrix')
X_node = tf.placeholder(tf.int32, shape=[batch_size], name='X_from_node_matrix')
Y = tf.placeholder(tf.float32, shape=[batch_size, 1], name='Y_label')

X_input = tf.Variable(word_mtx, dtype=tf.float32, name='X_for_word_vector')
X_weight = tf.Variable(node_mtx, dtype=tf.float32, name='X_for_node_vector')

para = 0

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    print(X_input.eval())
    print(X_weight.eval())
    for i in range(epoch):
        with open('train_skip_01_result.txt', 'r', encoding='utf-8') as fp_gb:
            while True:
                input1, input2, label = generate_batch(fp_gb)
                if not input1 or not input2: break
                label = np.array(label).reshape(batch_size, 1)
                embed1 = tf.nn.embedding_lookup(X_input, X_word)
                embed2 = tf.nn.embedding_lookup(X_weight, X_node)
                res1 = tf.matmul(embed1, embed2, transpose_b=True)
                a = list()
                for i in range(batch_size):
                    for j in range(batch_size):
                        if i==j:
                            a.append(res1[i, j])
                res1 = tf.convert_to_tensor(a, dtype=tf.float32)
                res1 = tf.reshape(res1, [batch_size, 1])
                cost = tf.nn.sigmoid_cross_entropy_with_logits(labels=Y, logits=res1)
                optimizer = tf.train.GradientDescentOptimizer(learning_rate=lrate).minimize(cost)
                _, cost_val = session.run([optimizer, cost], feed_dict={X_word:input1, X_node:input2, Y:label})
                para += 1
                if para%10==0:
                    print('hello, world %d' %para)
                    print('++++++', cost_val[0])
