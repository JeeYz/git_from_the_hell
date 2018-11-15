# @Author: JayY
# @Date:   2018-08-31T09:36:07+09:00
# @Filename: new_21.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:22:45+09:00
# @Copyright: JayY

# new_21.py
# making matrix with tensorflow
# ==========================================

import numpy as np
import tensorflow as tf

# 하나의 값으로 채우기
a = tf.constant(float(1/300), shape=[300, 300])
#b = tf.constant(0, shape=[300, 300])
# 단위 행렬 만들기
b = tf.constant(np.eye(300, dtype=float))
c = np.eye(300, dtype=float)

#init = tf.constant_initializer(c)

with tf.Session() as sess:
    #sess.run(init)
    print(sess.run(a))
    print(sess.run(b))
