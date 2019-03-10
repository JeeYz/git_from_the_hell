# @Author: JY
# @Date:   2019-02-18T16:15:51+09:00
# @Filename: e_28.py
# @Last modified by:   J.Y.
# @Last modified time: 2019-02-22T15:35:35+09:00
# @Copyright: JeeY

'''
this is basic system
transition based parsing
'''

import numpy as np
import tensorflow as tf
import copy

filename_00 = 'result_raw_words_list_00.words'
filename_01 = 'result_pos_temp_01.pos'
filename_02 = 'train_dataset_raw_02.train'
filename_03 = 'test_dataset_raw_02.test'

batch_size = 128
lrate = 0.05
epoch = 5

wordvec_size = 128
posvec_size = 73
word_num = 18
input_vector_size = (wordvec_size+posvec_size)*word_num

hidden_layer_size = 256
output_size = 3

full_train_list = list()
full_test_list = list()
pos_matrix = np.eye(posvec_size)

def generate_test_data():
    x_list = np.eye(test_data_size, input_vector_size)
    y_list = np.eye(test_data_size, output_size)
    for l,i in enumerate(range(test_data_size)):
        one_line = copy.deepcopy(full_test_list[i])
        xt_list = list()
        yt_list = list()
        for j,k in enumerate(one_line[:-1]):
            if j%2==0:
                xt_list.extend(word_matrix[k])
            else:
                xt_list.extend(pos_matrix[k])
        tmp = np.full((input_vector_size-len(xt_list)), 0)
        xt_list.extend(tmp)

        if one_line[-1]==0:
            yt_list = [1, 0, 0]
        elif one_line[-1]==1:
            yt_list = [0, 1, 0]
        elif one_line[-1]==2:
            yt_list = [0, 0, 1]

        x_list[l] = xt_list
        y_list[l] = yt_list
    return x_list, y_list

def generate_data(num):
    if (train_data_num-(batch_size*num)) >= batch_size:
        x_list = np.eye(batch_size, input_vector_size)
        y_list = np.eye(batch_size, output_size)
        for l,i in enumerate(range((batch_size*num), (batch_size*(num+1)))):
            one_line = copy.deepcopy(full_train_list[i])
            xt_list = list()
            yt_list = list()
            for j,k in enumerate(one_line[:-1]):
                if j%2==0:
                    xt_list.extend(word_matrix[k])
                else:
                    xt_list.extend(pos_matrix[k])
            tmp = np.full((input_vector_size-len(xt_list)), 0)
            xt_list.extend(tmp)

            if one_line[-1]==0:
                yt_list = [1, 0, 0]
            elif one_line[-1]==1:
                yt_list = [0, 1, 0]
            elif one_line[-1]==2:
                yt_list = [0, 0, 1]

            x_list[l] = xt_list
            y_list[l] = yt_list
    else:
        temp_batch_num = train_data_num-(batch_size*num)
        x_list = np.eye(batch_size, input_vector_size)
        y_list = np.eye(batch_size, output_size)
        for l,i in enumerate(range((batch_size*num), (batch_size*num+temp_batch_num))):
            one_line = copy.deepcopy(full_train_list[i])
            xt_list = list()
            yt_list = list()
            for j,k in enumerate(one_line[:-1]):
                if j%2==0:
                    xt_list.extend(word_matrix[k])
                else:
                    xt_list.extend(pos_matrix[k])
            tmp = np.full((input_vector_size-len(xt_list)), 0)
            xt_list.extend(tmp)

            if one_line[-1]==0:
                yt_list = [1, 0, 0]
            elif one_line[-1]==1:
                yt_list = [0, 1, 0]
            elif one_line[-1]==2:
                yt_list = [0, 0, 1]

            x_list[l] = xt_list
            y_list[l] = yt_list
            tnum = l
        for i in range(tnum+1, batch_size):
            x_list[i] = np.full([input_vector_size], 0)
            y_list[i] = np.full([output_size], 0)

    return x_list, y_list

word_matrix = dict()
pos_matrix = dict()

def make_word_matrix():
    para_num = 0
    with open(filename_00, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line: break
            line = line.split()
            word_matrix[para_num] = np.random.uniform(-1.0, 1.0, wordvec_size)
            para_num += 1
    para_num = 0
    temp_list = np.eye(posvec_size)
    with open(filename_01, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line: break
            line = line.split()
            pos_matrix[para_num] = temp_list[para_num]
            para_num += 1

def build_test_dataset():
    with open(filename_03, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line: break
            line = line.split()
            one_line = list()
            for i in line:
                one_line.append(int(i))
            full_test_list.append(one_line)
        return len(full_test_list)

def build_up_dataset():
    with open(filename_02, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line: break
            line = line.split()
            one_line = list()
            for i in line:
                one_line.append(int(i))
            full_train_list.append(one_line)
        return len(full_train_list)

make_word_matrix()
train_data_num = build_up_dataset()
test_data_size = build_test_dataset()
x_test_list, y_test_list = generate_test_data()

tf.set_random_seed(1)

input_X = tf.placeholder(tf.float32, [None, input_vector_size])
arc_Y = tf.placeholder(tf.float32, [None, output_size])

weight_0 = tf.Variable(tf.random_normal([input_vector_size, hidden_layer_size], stddev=1.0))
# hidden_layer_bias = tf.Variable(tf.random_uniform([batch_size, hidden_layer_size], -1.0, 1.0))

weight_1 = tf.Variable(tf.random_normal([hidden_layer_size, output_size], stddev=1.0))
# output_layer_bias = tf.Variable(tf.random_uniform([batch_size, output_size], -1.0, 1.0))

# h_res_0 = tf.nn.relu(tf.add(tf.matmul(input_X, weight_0), hidden_layer_bias))
# h_res_1 = tf.nn.relu(tf.add(tf.matmul(h_res_0, weight_1), output_layer_bias))

h_res_0 = tf.nn.relu(tf.matmul(input_X, weight_0))
h_res_1 = tf.nn.relu(tf.matmul(h_res_0, weight_1))

cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=arc_Y, logits=h_res_1))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=lrate).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    total_cost = 0.0
    para = 0
    for step in range(epoch):
        for i in range(int(train_data_num/batch_size)+1):
        # for i in range(600):
            x_list, y_list, = generate_data(i)
            _, loss_val = sess.run([optimizer, cost], feed_dict={input_X:x_list,
                                                                  arc_Y:y_list})
            total_cost += loss_val
            para += 1
            if i%100 == 0:
                lrate *= 0.999
                print('hello, world %d' %(para*batch_size),
                      '\t', 'learning rate %f' %lrate, '\t', 'mid. Avr. loss=', loss_val)
        print("Epoch = ", '%d' %step, 'ends. Avr. loss=', total_cost/batch_size)

        is_correct = tf.equal(tf.argmax(h_res_1, 1), tf.argmax(arc_Y, 1))
        accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
        print('정확도:', sess.run(accuracy, feed_dict={input_X: x_test_list,
                                                        arc_Y: y_test_list}))





















## endl
