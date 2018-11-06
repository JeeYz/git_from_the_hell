# @Author: JayY
# @Date:   2018-08-21T13:17:53+09:00
# @Filename: new_16.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:15:24+09:00
# @Copyright: JayY

# new_16.py
# practice tensorflow
# making matrix and print them

import tensorflow as tf
import numpy as np

a = np.array([2, 3], dtype=np.int32)
print(a)
b = np.array([4, 5], dtype=np.int32)
print(b)

c = tf.add(a, b)

with tf.Session() as sess:
    print(sess.run(c))
    print(c.eval())

x_vals = np.random.rand(2, 2)
print(x_vals)

x_var1 = tf.Variable(tf.random_uniform([5, 5], 0, 10))

#init = tf.global_variables_initializer()
init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(x_var1))
