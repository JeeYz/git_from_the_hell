# @Author: JY
# @Date:   2019-01-30T10:17:23+09:00
# @Filename: language_model_for_ETRI_data.py
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-11T02:45:18+09:00
# @Copyright: JeeY

######## ########## ############
# this file is for ETRI data
# making parsing
################################

##################
# embedding program
##################

import math
import tensorflow as tf
import numpy as np
import os
import copy
import sys
import random
import time
from datetime import datetime
sys.setrecursionlimit(10000)

num_of_train_data = 51200000
num_samples_negative = 10
batch_size = 256
word_vector_size = 256
epoch = 20
lrate = 0.005

data_para = 0

# filename00 = './data/korean_wiki/korean_wiki_result_words_01_after_reducing.txt'
filename01 = 'result_raw_words_list_temp_with_freq.words'

def count_number_of_words(filename_r):
    with open(filename_r, 'r', encoding='utf-8') as f:
        num_of_words = len(f.readlines())
    return num_of_words

num_of_words = count_number_of_words(filename01)
print(num_of_words)

def make_filename_list():
    filename_list = list()
    for (path, dir, files) in os.walk('./data/korean_wiki/'):
        for filename in files:
            if '.txt' in filename and 'korean_wiki_train_data_for_nce_' in filename:
                filename = path + '/' + filename
                filename_list.append(filename)
    return filename_list

filename_list = make_filename_list()
# print(filename_list)

def make_data(filename_r):
    with open(filename_r, 'r', encoding='utf-8') as f:
        data = f.read().split()
    return data

def generate_batch(data_para, length_data, data):
    cond = 1
    input1, input2 = list(), list()
    for i in range(batch_size):
        input1.append(int(data[data_para]))
        data_para += 1
        input2.append(int(data[data_para]))
        data_para += 1
        if (length_data-data_para) <= 0:
            data_para = 0
            cond = 0
    # input1 = np.array(input1)
    input2 = np.array(input2)
    input2 = np.reshape(input2, (batch_size, 1))
    return input1, input2, cond, data_para

#
# f_log = tf.gfile.FastGFile('negative_sampling_result_log.txt', 'a')
# f_log.write('\n' + '\n' + '\n')
# f_log.write('# ==============< Negative Sampling >=====================' + '\n')
# f_log.write('# negative sampling training for a file, \'skipgram_traindata_0.txt\'')
# f_log.write('\n' + '# starting time=' + str(datetime.now()) + '\n')
# f_log.write('# batch size=' + str(batch_size) + '\t' + 'word vector size=' + str(word_vector_size) + '\n')
# f_log.write('epoch=' + str(epoch) + '\t' + 'learning rate=' + str(lrate) + '\n')
# f_log.write('# ========================================================' + '\n')

tf.set_random_seed(1)


word_matrix = tf.random_uniform([num_of_words, word_vector_size], -1.0, 1.0)
center_word_p = tf.placeholder(tf.int32, shape=[batch_size], name='center_placeholder')
target_word_p = tf.placeholder(tf.int32, shape=[batch_size, 1], name='target_placeholder')

nce_weights = tf.Variable(tf.random_uniform([num_of_words, word_vector_size], -1.0, 1.0),
                          dtype=tf.float32, name='weights')
nce_biases = tf.Variable(tf.random_uniform([batch_size], -1.0, 1.0), dtype=tf.float32, name='bias_values')
center_word_v = tf.Variable(word_matrix, dtype=tf.float32, name='center_word_variable')

embedding = tf.nn.embedding_lookup(center_word_v, center_word_p, name='embadding')

saver_nce_skip = tf.train.Saver()
loss = tf.reduce_mean ( tf.nn.nce_loss(weights= nce_weights,
                                       biases = nce_biases,
                                       labels = target_word_p,
                                       inputs = embedding,
                                       num_sampled = num_samples_negative,
                                       num_classes = num_of_words ))
optimizer = tf.train.GradientDescentOptimizer (lrate).minimize(loss)

with tf.Session() as session:
    # saver_nce_skip = tf.train.Saver()
    if os.path.isdir('./nce_korean_wiki/'):
        for path, dir, files in os.walk('./nce_korean_wiki/'):
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == '.meta':
                    saver_nce_skip.restore(session, tf.train.latest_checkpoint('nce_korean_wiki'))
    else:
        os.mkdir('./nce_korean_wiki/')
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
                input1, input2, cond, data_para = generate_batch(data_para, length_data, data)
                if cond == 0: break
                _, loss_val = session.run([optimizer, loss], feed_dict={center_word_p:input1, target_word_p:input2})
                total_loss += loss_val
                para += 1
                if para%1000==0:
                    print('hello, world %d' %data_para, '\t', filename1,
                          '\t', '%dth epoch' %step, '\t', 'mid. Avr. loss=', loss_val)
            print("Epoch = ", '%d' %step, 'ends. Avr. loss=', total_loss/batch_size)
            saver_nce_skip.save(session, './nce_korean_wiki/korean_wiki_model_nce', global_step=step)
            skpt_state = tf.train.get_checkpoint_state("nce_korean_wiki")
        f_log.write("Epoch =" + str(step+1) + '\t' + 'ends. Avr. loss=' + str(total_loss/num_of_train_data*batch_size))
        f_log.write('\t' + 'time now = ' + str(datetime.now()) + '\n')






## endl
