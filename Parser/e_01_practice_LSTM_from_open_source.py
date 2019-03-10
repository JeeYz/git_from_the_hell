# @Author: JY
# @Date:   2019-01-08T15:21:07+09:00
# @Filename: e_01.py
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-11T00:43:36+09:00
# @Copyright: JeeY


import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
import numpy as np

mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

learning_rate = 0.001
total_epoch = 20
batch_size = 128

# one row size
n_inputs = 28
# lstm times
time_steps = 28
n_hidden = batch_size
# 1 ~ 10 classes
n_classes = 10

# X_input = tf.placeholder(tf.float32, [None, time_steps, n_input], name='one_row')
X_input = tf.placeholder(tf.float32, [None, time_steps, n_inputs], name='one_row')
Y_label = tf.placeholder(tf.float32, [None, n_classes], name='labels')

# input = tf.unstack(X_input, time_steps, 1)

weight = tf.Variable(tf.random_normal([n_hidden, n_classes]))
bias = tf.Variable(tf.random_normal([n_classes]))
#
# weights = {
#     # matrix from inputs (28) to hidden layer (128). shape is: (28, 128)
#     'in': tf.Variable(tf.random_normal([n_inputs, n_hidden_units])),
#     # matrix from hidden layer to output layer, shape is: (128, 10)
#     'out': tf.Variable(tf.random_normal([n_hidden_units, n_classes]))
# }
#
# biases = {
#     # bias for the input to hidden layer (128, )
#     'in': tf.Variable(tf.constant(0.1, shape=[n_hidden_units, ])),
#     # bias from the hidden to putput layer (10, )
#     'out': tf.Variable(tf.constant(0.1, shape=[n_classes, ]))
# }
#
# X = tf.reshape(X_input, [-1, n_inputs])
# X_in = tf.matmul(X, weights['in']) + biases['in']
# X_in = tf.reshape(X_in, [-1, time_steps, n_hidden_units])
#


LSTM_cell = tf.nn.rnn_cell.BasicLSTMCell(num_units=time_steps, dtype=tf.float32)
# outputs, state = tf.nn.static_rnn(LSTM_cell, input, dtype=tf.float32)
outputs, state = tf.nn.dynamic_rnn(LSTM_cell, X_input, dtype=tf.float32)
# outputs = tf.transpose(outputs, [1, 2, 0])
model = tf.matmul(outputs[-1], weight) + bias
predection = tf.nn.softmax(model)

# init_state = LSTM_cell.zero_state(batch_size, dtype=tf.float32)
#
# outputs, state = tf.nn.dynamic_rnn(LSTM_cell, X_in, initial_state=init_state, dtype=tf.float32)
#
# outputs = tf.unstack(tf.transpose(outputs, [1, 2, 0]))    # states is the last outputs
# results = tf.matmul(outputs[-1], weights['out']) + biases['out']
#
# # outputs = tf.transpose(outputs, [1, 0, 2])
# # outputs = outputs[-1]
# # model = tf.matmul(outputs, weight) + bias

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=prediction, labels=Y_label))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

######################
# Train Model
######################
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    total_batch = int(mnist.train.num_examples/batch_size)

    for epoch in range(total_epoch):
        total_cost = 0

        for i in range(total_batch):

            # for j in range(batch_size):
            #     batch_xs, batch_ys = mnist.train.next_batch(1)
            #     # X ?곗댄곕? RNN ????곗댄곗 留寃 [batch_size, n_step, n_input] ??濡 蹂??⑸??
            #     batch_xs = batch_xs.reshape((time_steps, n_input))
            #
            #     _, cost_val = sess.run([optimizer, cost],
            #                            feed_dict={X: batch_xs, Y: batch_ys})
            #     total_cost += cost_val

            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # X ?곗댄곕? RNN ????곗댄곗 留寃 [batch_size, n_step, n_input] ??濡 蹂??⑸??
            batch_xs = batch_xs.reshape((batch_size, time_steps, n_inputs))

            _, cost_val = sess.run([optimizer, cost],
                                   feed_dict={X_input: batch_xs, Y_label: batch_ys})
            total_cost += cost_val

        print('Epoch:', '%04d' % (epoch + 1),
              'Avg. cost =', '{:.3f}'.format(total_cost / total_batch))

    print('complete!')

#########
# Test
#########
is_correct = tf.equal(tf.argmax(model, 1), tf.argmax(Y_label, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

test_batch_size = len(mnist.test.images)
test_xs = mnist.test.images.reshape(test_batch_size, time_steps, n_input)
test_ys = mnist.test.labels

print('accuracy:', sess.run(accuracy,
                       feed_dict={X: test_xs, Y: test_ys}))







## end-line
