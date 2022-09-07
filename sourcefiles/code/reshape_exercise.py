# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np

a = np.random.randint(-10, 10, size=(1, 20, 20, 1))

a = np.asarray(a, dtype='float64')

# print(a)

@tf.function

x = tf.keras.layers.Conv2D(4, (2, 2), padding='same')(a)

# print(x)








