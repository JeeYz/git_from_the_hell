#####################
# this file is practice of tensorflow
# just exercise. 
# declare constants and print them with session.run
# and calculate of constants of tensor class
#####################



import numpy as np
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!!')
sess = tf.Session()

print(sess.run(hello))


with tf.Session() as sess:
    print(sess.run(hello))


a = tf.constant(2)
b = tf.constant(3)

with tf.Session() as sess:
    print("a : %i" % sess.run(a), "b : %i" % sess.run(b))
    print("Addition with constants : %i" % sess.run(a + b))
    print("Multiplication with constants : %i" % sess.run(a * b))


a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

add = tf.add(a, b)
mul = tf.multiply(a, b)

with tf.Session() as sess:
    print(sess.run(add, feed_dict={a: 2, b: 3}))
    print(sess.run(mul, feed_dict={a: 2, b: 3}))


matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])
product = tf.matmul(matrix1, matrix2)

print(product)

with tf.Session() as sess:
    result = sess.run(product)
    print(result)
