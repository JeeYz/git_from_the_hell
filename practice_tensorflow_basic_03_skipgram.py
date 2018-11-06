# @Author: JayY
# @Date:   2018-09-06T14:26:10+09:00
# @Filename: new_23.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:26:55+09:00
# @Copyright: JayY

# new_23.py
# pratice embedding_lookup functions
# practicing for making skipgram algorithm
# ==========================================

'''
practice for embedding_lookup
'''

import numpy as np
import random
import tensorflow as tf

matrix = np.random.random([1024, 64])
ids = np.array([0, 5, 17, 33])

param1 = tf.constant([10, 20, 30, 40])
param2 = tf.constant([1, 2, 3, 4])
ids1 = tf.constant([0, 1, 2, 3])
ids2 = tf.constant([2, 3, 0, 0])

with tf.Session() as session:
    print(tf.nn.embedding_lookup(param1, ids1).eval())
    print(tf.nn.embedding_lookup(param1, ids2).eval())
    print(tf.nn.embedding_lookup([param1, param2], ids1).eval())
    print(tf.nn.embedding_lookup([param1, param2], ids2).eval())

f = open("example03.txt", 'r', encoding='utf-8')

d = list()
while True:
    c = list()
    a = f.readline()
    if not a: break
    b = a.split()
    for i in b:
        i = float(i)
        c.append(i)
    c = np.array(c)
    d.append(c)

x_data = np.array(d)
x_num = [1, 5, 6, 3, 7]
print(x_data.shape, type(x_data))

X_p = tf.placeholder(tf.int32, shape=[5])
X_v = tf.Variable(x_data, dtype=tf.float32)
embed = tf.nn.embedding_lookup(X_v, X_p)

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    session.run(embed, feed_dict={X_p: x_num})
    print(embed)
