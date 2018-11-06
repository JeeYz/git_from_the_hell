# @Author: JayY
# @Date:   2018-08-20T10:04:56+09:00
# @Filename: new_14.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T14:36:38+09:00
# @Copyright: JayY

# new_14.py
# simple neural network for classifying MNIST

import numpy as np
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

input_mnist = 28*28
hidden_00 = 256
lrate = 0.01
batch_size = 100

X = tf.placeholder(tf.float32, [None, input_mnist])
Y = tf.placeholder(tf.float32, [None, 10])

W1 = tf.Variable(tf.random_normal([input_mnist, hidden_00], stddev=0.01))
L1 = tf.nn.relu(tf.matmul(X, W1))

W2 = tf.Variable(tf.random_normal([hidden_00, 10], stddev=0.01))
model = tf.matmul(L1, W2)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=model, labels=Y))
#optimizer = tf.train.AdamOptimizer(lrate).minimize(cost)
optimizer = tf.train.GradientDescentOptimizer(lrate).minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

total_batch = 500

for epoch in range(100):
    total_cost = 0

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        _, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs, Y: batch_ys})
        total_cost += cost_val

    print('Epoch:', '%04d' % (epoch + 1),
          'Avg. cost =', '{:.3f}'.format(total_cost / total_batch))

is_correct = tf.equal(tf.argmax(model, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

print('정확도:', sess.run(accuracy,
                        feed_dict={X: mnist.test.images,
                                   Y: mnist.test.labels}))
