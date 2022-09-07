# @Author: JY
# @Date:   2019-02-19T11:35:42+09:00
# @Filename: e_31.py
# @Last modified by:   JeeY
# @Last modified time: 2019-02-22T04:36:31+09:00
# @Copyright: JeeY

import numpy as np
# import tensorflow as tf

# print(np.eye(73))

# list_a = [j for j in range(10)]
# list_b = [i for i in range(10)]
# print(list_a)
# print(list_b)
#
# list_a = tf.constant(list_a)
# list_b = tf.constant(list_b)
# list_c = tf.concat(list_a, list_b, 1)
#
# with tf.Session() as sess:
#     print(sess.run(list_c))

temp_list = np.eye(10)
print(temp_list)

# tmp_list = np.eye(10, 5)
# print(tmp_list)
tmp_list = list()
for i in range(10):
    tmp_list[i] = list()
    tmp_list[i] = [j for j in range(10)]
print(tmp_list)
# num = int(10/3)
#
# for i in range(num+1):
#     print(i)


## endl
