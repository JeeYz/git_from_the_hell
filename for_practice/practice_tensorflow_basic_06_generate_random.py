# @Author: JayY <JeeYz>
# @Date:   2018-08-09T15:28:41+09:00
# @Filename: new_06.py
# @Last modified by:   JeeYz
# @Last modified time: 2018-11-02T13:59:59+09:00
# @Copyright: JayY

# new_06.py
# generate random values with numpy && tensorflow

import numpy as np
import tensorflow as tf

a = np.random.random((5, 5))
b = np.random.randint(0, 20, (5, 1))

print(a, b)
print(np.dot(a, b))

x = tf.constant(a, dtype=tf.float32)
y = tf.constant(b, dtype=tf.float32)

print(x, y)
z = tf.matmul(x, y)

with tf.Session() as sess:
    print(sess.run(x))
    print(sess.run(y))
    print(sess.run(z))

a = tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3])
b = tf.constant([7, 8, 9, 10, 11, 12], shape=[3, 2])
print(a, b)
c = tf.matmul(a, b)
print(c)
with tf.Session() as sess:
    print(sess.run(c))
a = tf.constant(np.arange(1, 13, dtype=np.int32), shape=[2, 2, 3])
b = tf.constant(np.arange(13, 25, dtype=np.int32), shape=[2, 3, 2])
print(a, b)
c = tf.matmul(a, b)
print(c)
