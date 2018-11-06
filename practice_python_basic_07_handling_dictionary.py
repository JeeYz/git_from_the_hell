# @Author: JayY
# @Date:   2018-08-10T15:20:10+09:00
# @Filename: new_07.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T15:48:54+09:00
# @Copyright: JayY


# new_07.py
# making dictionary and handle it

import tensorflow as tf
import numpy as np

a = tf.random_uniform([2, 3], -1, 1, dtype=tf.float32)
print(a)


with tf.Session() as sess:
    print(sess.run(a))


dictinary = dict()

print(dictinary)


class node():
    pass

dictionary = {a: (1, 2, 3)}
print(dictionary)
dictionary

dictionary = {'a': (1, 2, 3)}
print(dictionary)

dictionary = {'a': [1, 2, 3]}
print(dictionary)

print(dictionary['a'])

dictionary.keys()
dictionary.values()

dictionary['b']= [4, 5, 6]
print(dictionary)
dictionary['a'][2] = 10
print(dictionary)
