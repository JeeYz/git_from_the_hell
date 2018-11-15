# @Author: JayY
# @Date:   2018-10-12T14:55:03+09:00
# @Filename: modified_01.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T17:05:10+09:00
# @Copyright: JayY



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

batch_size = 128
word_vector_size = 300
epoch = 10
lrate = 0.005

data_para = 0

def make_filename_list():
    filename_list = list()
    for (path, dir, files) in os.walk('./'):
        for filename in files:
            if '.txt' in filename and 'skipgram_traindata_' in filename:
                filename_list.append(filename)
    return filename_list

filename_list = make_filename_list()
print(filename_list)
def build_dataset():
    with open("result_03.txt", 'r', encoding='utf-8') as f:
        num_word = len(f.readlines())
        word_mtx = list()
        for i in range(num_word):
            a = np.random.uniform(-1.0, 1.0, word_vector_size)
            word_mtx.append(a)
    with open("result_04.txt", 'r', encoding='utf-8') as f:
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

word_mtx, node_mtx = build_dataset()

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

saver = tf.train.Saver()

embed1 = tf.nn.embedding_lookup(X_input, X_word)
embed2 = tf.nn.embedding_lookup(X_weight, X_node)

m_res = tf.multiply(embed1, embed2)
l_res = tf.reduce_sum(m_res, 1)
n_res = tf.add(l_res, bias)

cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=Y, logits=n_res))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=lrate).minimize(cost)

with tf.Session() as session:
    if os.path.isdir('./skip_gram/'):
        for path, dir, files in os.walk('./skip_gram/'):
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == '.meta':
                    saver.restore(session, tf.train.latest_checkpoint('skip_gram'))
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
            f_log.write("Epoch =" + str(step+1) + '\t' + 'ends. Avr. loss=' + str(total_loss/batch_size))
            f_log.write('\t' + 'time now = ' + str(datetime.now()) + '\n')
            print("Epoch = ", '%d' %step, 'ends. Avr. loss=', total_loss/batch_size)
        saver.save(session, './skip_gram/my_test_model', global_step=step)
    skpt_state = tf.train.get_checkpoint_state("skip_gram")
