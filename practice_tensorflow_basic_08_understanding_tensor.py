# @Author: JayY
# @Date:   2018-06-21T09:52:33+09:00
# @Filename: tensor_01.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T16:23:50+09:00
# @Copyright: JayY



import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
print(hello)

a = tf.constant(10)
b = tf.constant(32)
c = tf.add(a, b)
print(c)

sess = tf.Session()

print(sess.run(hello))
print(sess.run([a, b, c]))

sess.close()

X = tf.placeholder(tf.float32, [None, 3])
print(X)

x_data = [[1, 2, 3], [4, 5, 6]]

W = tf.Variable(tf.random_normal([3, 2]))
b = tf.Variable(tf.random_normal([2, 1]))

expr = tf.matmul(X, W) + b

sess = tf.Session()
sess.run(tf.global_variables_initializer())

print("=== x_data ===")
print(x_data)
print("=== W ===")
print(sess.run(W))
print("=== b ===")
print(sess.run(b))
print("=== expr ===")

print(sess.run(expr, feed_dict={X: x_data}))

sess.close()
