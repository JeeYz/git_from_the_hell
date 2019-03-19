# @Author: J.Y.
# @Date:   2019-03-19T12:33:32+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-19T15:00:40+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import tensorflow as tf
import numpy as np
import time
import sys
import os

train_files = list()
for (path, dir, files) in os.walk("d:/Program_Data/"):
    for filename in files:
        if 'result_train_dataset_' in filename:
            train_files.append(filename)
train_files = tuple(train_files)

sys.path.append(r'c:/Users/AI_LAB/Desktop/Github/git_from_the_hell/Keras_parsing/module')
import keras_module_0 as k0

batch_size = 128
epochs = 5
w_vec_size = 128
p_vec_size = 73
lrate = 0.05

input_vector_size = 18*w_vec_size + 18*p_vec_size
hidden_layer_size = 512
output_size = 3

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
    for step in range(epochs):
        for j in train_files:
            filename = 'd:/Program_Data/' + j
            x_data, y_data, train_data_num = k0.generate_train_data(filename)
            for i in range(int(train_data_num/batch_size)+1):
                x_list, y_list = k0.divide_train_data(x_data, y_data, i, batch_size, train_data_num)
                _, loss_val = sess.run([optimizer, cost], feed_dict={input_X:x_list,\
                                                                      arc_Y:y_list})
                total_cost += loss_val
                para += 1
                if i%100 == 0:
                    # lrate *= 0.999
                    print('hello, world %d' %(para*batch_size),
                          '\t', 'learning rate %f' %lrate, '\t', 'mid. Avr. loss=', loss_val)
        print("Epoch = ", '%d' %step, 'ends. Avr. loss=', total_cost/batch_size)

    # is_correct = tf.equal(tf.argmax(h_res_1, 1), tf.argmax(arc_Y, 1))
    # accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
    # print('정확도:', sess.run(accuracy, feed_dict={input_X: x_test_list,
    #                                                     arc_Y: y_test_list}))













## endl
