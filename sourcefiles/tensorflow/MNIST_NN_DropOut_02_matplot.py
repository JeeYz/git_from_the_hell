# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 11:03:27 2018

@author: JeeY
"""

#%%
import tensorflow as tf
import numpy as np
import datetime
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

fw = open("MNIST_NN_DropOut_01_result.txt", 'a')

input_mnist = 28*28
hidden_00 = 256
hidden_01 = 256
lrate = 0.0002
batch_size = 100
dropout_rate = 0.8
s = datetime.datetime.now()


#%%
fw.write("\n\n\n")
fw.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")
fw.write("# " + str(s) + "\n")
fw.write("# MNIST Simple Deep Neural Network with Drop Out \n")
fw.write('# Number of Hidden 00 : ' + str(hidden_00))
fw.write("\t")
fw.write('# Number of Hidden 01 : ' + str(hidden_01))
fw.write("\n")
fw.write('# Learning Rate :' + str(lrate) + '\t' + 'Batch Size :' + str(batch_size))
fw.write("\t"+"DropOut Rate : " + str(dropout_rate) + "\n")
fw.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")

#%%
X = tf.placeholder(tf.float32, [None, input_mnist])
Y = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)


W1 = tf.Variable(tf.random_normal([input_mnist, hidden_00], stddev=0.01))
L1 = tf.nn.relu(tf.matmul(X, W1))
L1 = tf.nn.dropout(L1, keep_prob)

W2 = tf.Variable(tf.random_normal([hidden_00, hidden_01], stddev=0.01))
L2 = tf.nn.relu(tf.matmul(L1, W2))
L2 = tf.nn.dropout(L2, keep_prob)

W3 = tf.Variable(tf.random_normal([hidden_01, 10], stddev=0.01))
model = tf.matmul(L2, W3)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=model, labels=Y))
optimizer = tf.train.AdamOptimizer(lrate).minimize(cost)


#%%
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

total_batch = int(mnist.train.num_examples / batch_size)

for epoch in range(15):
    total_cost = 0
    
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        
        _, cost_val = sess.run([optimizer, cost],
                               feed_dict={X: batch_xs, Y: batch_ys,
                                          keep_prob: dropout_rate})
        total_cost += cost_val
        
    print('Epoch:', '%04d' % (epoch + 1),
          'Avg. cost =', '{:3f}'.format(total_cost / total_batch))
    fw.write('Epoch:' + '%04d' % (epoch + 1) +
          'Avg. cost =' + '{:3f}'.format(total_cost / total_batch) + "\n")
    
print('complete!!')
fw.write('complete!!\n')

#%%
is_correct = tf.equal(tf.argmax(model, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

print('accuracy:', sess.run(accuracy,
                            feed_dict={X: mnist.test.images,
                                       Y: mnist.test.labels,
                                       keep_prob: 1}))
fw.write('accuracy:' + str(sess.run(accuracy,
                        feed_dict={X: mnist.test.images,
                                   Y: mnist.test.labels,
                                   keep_prob: 1})))
fw.write("\n\n\n\n\n\n")


#%%
labels = sess.run(model,
                  feed_dict={X: mnist.test.images,
                             Y: mnist.test.labels,
                             keep_prob: 1})
    
fig = plt.figure()
for i in range(10):
    subplot = fig.add_subplot(2, 5, i + 1)
    subplot.set_xticks([])
    subplot.set_yticks([])
    subplot.set_title('%d' % np.argmax(labels[i]))
    subplot.imshow(mnist.test.images[i].reshape((28, 28)),
                   cmap=plt.cm.gray_r)
    
plt.show()

fw.close()


#%%

























