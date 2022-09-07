# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:37:21 2018

@author: JeeY
"""


#%%
import tensorflow as tf
import datetime

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

s = datetime.datetime.now()
window_size = 28 
learning_rate = 0.001
batch_size = 100
dropout_rate = 0.7

#%%
fw = open("MNIST_CNN_03_API_result.txt", "a")
fw.write("\n\n\n")
fw.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")
fw.write("# " + str(s) + "\n")
fw.write("# MNIST Convolutional Neural Network with Drop Out \n")
fw.write('# Window Size : ' + str(window_size))
fw.write("\n")
fw.write("# Batch Size : " + str(batch_size) + "\t" + "Dropout Rate : " + str(dropout_rate))
fw.write("\n")
fw.write("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")
fw.write("\n")
         
#%%
X = tf.placeholder(tf.float32, [None, window_size, window_size, 1])
Y = tf.placeholder(tf.float32, [None, 10])
is_training = tf.placeholder(tf.bool)


#%%
L1 = tf.layers.conv2d(X, 32, [3, 3])
L1 = tf.layers.max_pooling2d(L1, [2, 2], [2, 2])
L1 = tf.layers.dropout(L1, dropout_rate, is_training)

L2 = tf.layers.conv2d(L1, 64, [3, 3])
L2 = tf.layers.max_pooling2d(L2, [2, 2], [2, 2])
L2 = tf.layers.dropout(L2, dropout_rate, is_training)

L3 = tf.contrib.layers.flatten(L2)
L3 = tf.layers.dense(L3, 256, activation=tf.nn.relu)
L3 = tf.layers.dropout(L3, 0.5, is_training)

model = tf.layers.dense(L3, 10, activation=None)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
	logits=model, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

#%%
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

total_batch = int(mnist.train.num_examples / batch_size)


#%%
for epoch in range(15):
    total_cost = 0
    
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs = batch_xs.reshape(-1, window_size, window_size, 1)
        
        _, cost_val = sess.run([optimizer, cost],
                               feed_dict = {X: batch_xs,
                                            Y: batch_ys,
                                            is_training: True})
        total_cost += cost_val
    
    print('Epoch:', '%04d'%(epoch+1),
          'Avg.cost = ', '{:.4f}'.format(total_cost / total_batch))
    fw.write('Epoch:' + '%04d'%(epoch+1) +
          'Avg.cost = ' + '{:.4f}'.format(total_cost / total_batch) + '\n')
    
print("최적화 완료!!")
fw.write("최적화 완료!!\n")


#%%
is_correct = tf.equal(tf.argmax(model, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('정확도:', sess.run(accuracy,
feed_dict={X: mnist.test.images.reshape(-1, window_size, window_size, 1), 
           Y: mnist.test.labels, 
           is_training: False}))
    
fw.write('정확도:' + str(sess.run(accuracy, 
                           feed_dict={X: mnist.test.images.reshape(-1, 28, 28, 1), 
                                      Y: mnist.test.labels, is_training: False})))
    
    
    
