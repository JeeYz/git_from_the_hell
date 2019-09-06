# @Author: J.Y.
# @Date:   2019-05-16T10:16:28+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-09-06T10:08:25+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

from keras import backend as K
from keras.engine.topology import Layer
from keras import initializers
from keras import models
from keras.layers import Lambda
from keras.layers import Dense, Dropout
from keras import layers
from keras import activations
import numpy as np

NUM_OF_NEURONS = 512

def find_softmax(tensors):
    return activations.softmax(tensors, axis=-1)

def output_of_lambda(input_shape):
    return (input_shape[0], input_shape[1])


class Dozat(Layer):

    def __init__(self, output_dim, **kwargs):
        self.output_dim = output_dim
        super(Dozat, self).__init__(**kwargs)

    def call(self, x):
        m = K.random_uniform_variable((NUM_OF_NEURONS, NUM_OF_NEURONS), 0, 1, seed=1)

        # x = Dropout(rate=0.4)(x)
        x = Dropout(rate=0.8)(x)
        a = layers.Dense(NUM_OF_NEURONS, activation='relu')(x)
        b = layers.Dense(NUM_OF_NEURONS, activation='relu')(x)
        b = K.permute_dimensions(b, (0, 2, 1))

        # print(K.int_shape(a))
        K.expand_dims(a, axis=-1)
        # print(K.int_shape(a))
        # print('a : ', a, '\n')
        # print('b : ', b, '\n')
        # print('m : ', m, '\n\n\n')
        x = K.dot(a, m)
        x = K.batch_dot(x, b)
        # print('x : ', x, '\n\n\n')
        x = Lambda(find_softmax, output_shape=output_of_lambda)(x)
        # print('x : ', x, '\n\n\n')
        return x

    def compute_output_shape(self, input_shape):
        return (1, self.output_dim, self.output_dim)


class Dozat_t(Layer):

    def __init__(self, output_dim, **kwargs):
        self.output_dim = output_dim
        super(Dozat_t, self).__init__(**kwargs)

    def call(self, x):
        m = K.random_uniform_variable((NUM_OF_NEURONS, NUM_OF_NEURONS), 0, 1, seed=1)

        # x = Dropout(rate=0.4)(x)
        # x = Dropout(rate=0.4)(x)
        a = layers.Dense(NUM_OF_NEURONS, activation='relu')(x)
        b = layers.Dense(NUM_OF_NEURONS, activation='relu')(x)
        b = K.permute_dimensions(b, (0, 2, 1))

        # print(K.int_shape(a))
        K.expand_dims(a, axis=-1)
        # print(K.int_shape(a))
        # print('a : ', a, '\n')
        # print('b : ', b, '\n')
        # print('m : ', m, '\n\n\n')
        x = K.dot(a, m)
        x = K.batch_dot(x, b)
        # print('x : ', x, '\n\n\n')
        x = Lambda(find_softmax, output_shape=output_of_lambda)(x)
        # print('x : ', x, '\n\n\n')
        return x

    def compute_output_shape(self, input_shape):
        return (1, self.output_dim, self.output_dim)










if __name__ == '__main__':
    print('hello, world~!')

## endl
