# @Author: JY
# @Date:   2019-01-11T10:54:09+09:00
# @Filename: e_03.py
# @Last modified by:   J.Y.
# @Last modified time: 2019-02-21T11:20:18+09:00
# @Copyright: JeeY

""" Long Short Term Memory for MNIST """

import tensorflow as tf
# from tensorflow.contrib import rnn

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# print(int(mnist.train.num_examples))

learning_rate = 0.001
training_steps = 30000
batch_size = 128
display_step = 200 # ??

num_input = 28
timesteps = 28
num_hidden = 128
num_classes = 10

X_input = tf.placeholder(tf.float32, shape=[None, timesteps, num_input])
Y_label = tf.placeholder(tf.float32, shape=[None, num_classes])

weights = tf.Variable(tf.random_normal([num_hidden, num_classes]))
biases = tf.Variable(tf.random_normal([num_classes]))

def RNN(x, weights, biases):

    # Prepare data shape to match `rnn` function requirements
    # Current data input shape: (batch_size, timesteps, n_input)
    # Required shape: 'timesteps' tensors list of shape (batch_size, n_input)

    # Unstack to get a list of 'timesteps' tensors of shape (batch_size, n_input)
    x = tf.unstack(x, timesteps, 1)

    # Define a lstm cell with tensorflow
    lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(num_hidden, forget_bias=1.0)

    # Get lstm cell output
    outputs, states = tf.nn.static_rnn(lstm_cell, x, dtype=tf.float32)

    # Linear activation, using rnn inner loop last output
    return tf.matmul(outputs[-1], weights) + biases

logits = RNN(X_input, weights, biases)
prediction = tf.nn.softmax(logits)

# Define loss and optimizer
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    logits=logits, labels=Y_label))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(loss)

# Evaluate model (with test logits, for dropout to be disabled)
correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y_label, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for step in range(1, training_steps+1):
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        batch_x = batch_x.reshape((batch_size, timesteps, num_input))
        sess.run(train_op, feed_dict={X_input: batch_x, Y_label: batch_y})

        if step % display_step == 0 or step == 1:
            loss_val, acc = sess.run([loss, accuracy], feed_dict={X_input: batch_x, Y_label: batch_y})
            print("Step " + str(step) + ", Minibatch Loss= " + \
                  "{:.4f}".format(loss_val) + ", Training Accuracy= " + \
                  "{:.3f}".format(acc))

    print("Optimization Finished!")

    test_len = 128
    test_data = mnist.test.images[:test_len].reshape((-1, timesteps, num_input))
    test_label = mnist.test.labels[:test_len]
    print("Testing Accuracy:", \
        sess.run(accuracy, feed_dict={X_input: test_data, Y_label: test_label}))




## end-line
