# @Author: Jay <JeeYz>
# @Date:   2018-10-30T11:21:29+09:00
# @Filename: skip_gram_model_00.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-19T11:59:14+09:00
# @Copyright: JayY

# this is completed
# skipgram I made Ver.1.0.0

# =================== Ver.1.1.0 ========================================
# change save data file
# rename parameter folder : skip_gram -> skip_gram_korean_wiki
# this version for korean wiki data
# ======================================================================

import os
import time
import collections
import tensorflow as tf
import numpy as np
import random
import copy
import sys

from datetime import datetime
sys.setrecursionlimit(50000)

num_of_train_data = 51200000
batch_size = 128
word_vector_size = 300
epoch = 20
lrate = 0.01

data_para = 0

def make_filename_list():
    filename_list = list()
    for (path, dir, files) in os.walk('./data/'):
        for filename in files:
            if '.txt' in filename and 'korean_wiki_skipgram_traindata_' in filename:
                filename = path + '/' + filename
                filename_list.append(filename)
    return filename_list

filename_list = make_filename_list()
# print(filename_list)

filename00 = './data/korean_wiki/korean_wiki_result_words_02_huff_words.txt'
filename01 = './data/korean_wiki/korean_wiki_result_words_03_huff_nodes.txt'

def build_dataset(filename_r1, filename_r2):
    with open(filename_r1, 'r', encoding='utf-8') as f:
        num_word = len(f.readlines())
        word_mtx = list()
        for i in range(num_word):
            a = np.random.uniform(-1.0, 1.0, word_vector_size)
            word_mtx.append(a)
    with open(filename_r2, 'r', encoding='utf-8') as f:
        num_node = len(f.readlines())
        node_mtx = list()
        for i in range(num_node):
            a = np.random.uniform(-1.0, 1.0, word_vector_size)
            node_mtx.append(a)
    word_mtx = np.array(word_mtx).reshape(-1, word_vector_size)
    node_mtx = np.array(node_mtx).reshape(-1, word_vector_size)
    print(type(word_mtx), word_mtx.shape)
    print(type(node_mtx), node_mtx.shape)
    return word_mtx, node_mtx

word_mtx, node_mtx = build_dataset(filename00, filename01)

def make_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read().split()
    return data

def generate_batch(data_para, length_data, data):
    cond = 1
    input1, input2, label = list(), list(), list()
    for i in range(batch_size):
        input1.append(int(data[data_para]))
        data_para += 1
        input2.append(int(data[data_para]))
        data_para += 1
        label.append(data[data_para])
        data_para += 1
        if (length_data-data_para) <= 0:
            data_para = 0
            cond = 0
    label = np.array(label)
    return input1, input2, label, cond, data_para

f_log = tf.gfile.FastGFile('skip_gram_result_log.txt', 'a')

f_log.write('\n' + '\n' + '\n')
f_log.write('#######################################################' + '\n')
f_log.write('skipgram training for a file, \'skipgram_traindata_0.txt\'')
f_log.write('\n' + 'starting time=' + str(datetime.now()) + '\n')
f_log.write('batch size=' + str(batch_size) + '\t' + 'word vector size=' + str(word_vector_size) + '\n')
f_log.write('epoch=' + str(epoch) + '\t' + 'learning rate=' + str(lrate) + '\n')
f_log.write('#######################################################' + '\n')

tf.set_random_seed(1)
X_word = tf.placeholder(tf.int32, shape=[batch_size], name='X_from_word_matrix')
X_node = tf.placeholder(tf.int32, shape=[batch_size], name='X_from_node_matrix')
Y = tf.placeholder(tf.float32, shape=[batch_size], name='Y_label')

X_input = tf.Variable(word_mtx, dtype=tf.float32, name='X_for_word_vector')
X_weight = tf.Variable(node_mtx, dtype=tf.float32, name='X_for_node_vector')
bias = tf.Variable(tf.random_uniform([batch_size], -1.0, 1.0), dtype=tf.float32, name='bias_values')

saver_hier_skip = tf.train.Saver()

embed1 = tf.nn.embedding_lookup(X_input, X_word)
embed2 = tf.nn.embedding_lookup(X_weight, X_node)

m_res = tf.multiply(embed1, embed2)
l_res = tf.reduce_sum(m_res, 1)
n_res = tf.add(l_res, bias)

cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=Y, logits=n_res))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=lrate).minimize(cost)

with tf.Session() as session:
    if os.path.isdir('./skip_gram_korean_wiki/'):
        for path, dir, files in os.walk('./skip_gram_korean_wiki/'):
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == '.meta':
                    saver_hier_skip.restore(session, tf.train.latest_checkpoint('skip_gram_korean_wiki'))
    else:
        session.run(tf.global_variables_initializer())

    for step in range(epoch):
        para = 0
        total_loss = 0.0
        print('hello, world')
        for filename1 in filename_list:
            print(filename1)
            data = make_data(filename1)
            length_data = len(data)
            data_para = 0
            cond = 1
            while cond==1:
                input1, input2, label, cond, data_para = generate_batch(data_para, length_data, data)
                if cond == 0: break
                _, cost_val = session.run([optimizer, cost], feed_dict={X_word:input1, X_node:input2, Y:label})
                total_loss += cost_val
                para += 1
                if para%1000==0:
                    print('hello, world %d' %data_para, '\t', filename1,
                          '\t', '%dth epoch' %step, '\t', 'mid. Avr. loss=', cost_val)
            print("Epoch = ", '%d' %step, 'ends. Avr. loss=', total_loss/batch_size)
            saver_hier_skip.save(session, './skip_gram_korean_wiki/korean_wiki_model', global_step=step)
            skpt_state = tf.train.get_checkpoint_state("skip_gram_korean_wiki")
        f_log.write("Epoch =" + str(step+1) + '\t' + 'ends. Avr. loss=' + str(total_loss/num_of_train_data*batch_size))
        f_log.write('\t' + 'time now = ' + str(datetime.now()) + '\n')
