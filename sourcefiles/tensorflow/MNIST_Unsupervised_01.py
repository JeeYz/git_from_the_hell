# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 12:28:29 2018

@author: JeeY
"""

#%%
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import datetime

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

#fwp = open("MNIST_Unsupervised_01_result.txt", "a")

#%%
learning_rate = 0.01
training_epoch = 20
batch_size = 100
n_hidden = 256
n_input = 28*28
sample_size = 10
s = datetime.datetime.now()


#%%
#fwp = open("MNIST_Unsupervised_01_result.txt", "a")
#fwp.write("\n\n\n")
#fwp.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")
#fwp.write("# " + str(s) + "\n")
#fwp.write("# MNIST Unsupervised learning as known Autoencoder \n")
#fwp.write('# n_hidden : ' + str(n_hidden) + "\t" + 'n_input : ' + str(n_input) )
#fwp.write('Sample Size : ' + str(sample_size))
#fwp.write("\n")
#fwp.write("# Batch Size : " + str(batch_size) + "\t" + "Learning Rate : " + str(learning_rate))
#fwp.write("Training Epoch : " + str(training_epoch))
#fwp.write("\n")
#fwp.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")
#fwp.write("\n")


#%%
X = tf.placeholder(tf.float32, [None, n_input])

W_encode = tf.Variable(tf.random_normal([n_input, n_hidden]))
b_encode = tf.Variable(tf.random_normal([n_hidden]))
encoder = tf.nn.sigmoid(tf.add(tf.matmul(X, W_encode), b_encode))

W_decode = tf.Variable(tf.random_normal([n_hidden, n_input]))
b_decode = tf.Variable(tf.random_normal([n_input]))
decoder = tf.nn.sigmoid(tf.add(tf.matmul(encoder, W_decode), b_decode))

cost = tf.reduce_mean(tf.pow(X - decoder, 2))
optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(cost)


#%%
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

total_batch = int(mnist.train.num_examples / batch_size)


#%%
for epoch in range(training_epoch):
    total_cost = 0
    
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        _, cost_val = sess.run([optimizer, cost],
                               feed_dict = {X: batch_xs})
        total_cost += cost_val
        
    print('Epoch:', '%04d'%(epoch + 1),
              'Avg.cost = ', '{:.4f}'.format(total_cost / total_batch))
#    fwp.write('Epoch:' + '%04d'%(epoch + 1) + 
#              'Avg.cost = ' + '{:.4f}'.format(total_cost / total_batch) + '\n')
        
print('최적화 완료!!')
#fwp.write('최적화 완료!!\n')


#%%
samples = sess.run(decoder,
                   feed_dict = {X: mnist.test.images[:sample_size]})

fig, ax = plt.subplots(2, sample_size, figsize = (sample_size, 2))

for i in range(sample_size):
    ax[0][i].set_axis_off()
    ax[1][i].set_axis_off()
    ax[0][i].imshow(np.reshape(mnist.test.images[i], (28, 28)))
    ax[1][i].imshow(np.reshape(samples[i], (28, 28)))
    
    
plt.show()

#%%







