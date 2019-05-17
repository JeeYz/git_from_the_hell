# @Author: J.Y.
# @Date:   2019-05-16T10:16:28+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-17T12:01:07+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

from keras import backend as K
from keras.engine.topology import Layer
from keras import initializers
from keras import models
from keras.layers import Lambda
from keras.layers import Dense, Dropout
from keras import layers

import numpy as np

W_VEC_SIZE = 128

def find_argmax(tensors):
    return K.argmax(tensors, axis=1)

def output_of_lambda(input_shape):
    return (input_shape[0], input_shape[1])


class Dozat(Layer):

    def __init__(self, output_dim, **kwargs):
        self.output_dim = output_dim
        super(Dozat, self).__init__(**kwargs)

    # def __init__(self, a, b, output_dim, **kwargs):
    #     self.a = a
    #     self.b = b
    #     self.output_dim = output_dim
    #     super(Dozat, self).__init__(**kwargs)

    def call(self, x):
        m = K.random_uniform_variable((128, 128), 0, 1, seed=1)

        x = Dropout(rate=0.4)(x)
        a = layers.Dense(W_VEC_SIZE, activation='relu')(x)
        b = layers.Dense(W_VEC_SIZE, activation='relu')(x)
        b = K.permute_dimensions(b, (0, 2, 1))

        x = K.dot(a, m)
        x = K.batch_dot(x, b)

        # x = K.dot(self.a, m)
        # x = K.batch_dot(x, self.b)

        # x = K.dot(l[0], m)
        # x = K.batch_dot(x, l[1])

        # x = K.argmax(x, axis=-1)
        x = Lambda(find_argmax, output_shape=output_of_lambda)(x)
        # x = Lambda(lambda x:K.argmax(x, axis=-1))(x)
        # x = Lambda(lambda x:x)(x)
        # x = Lambda(x)(x)
        return x

    def compute_output_shape(self, input_shape):
        return (1, self.output_dim)











if __name__ == '__main__':
    print('hello, world~!')

## endl
