# @Author: J.Y.
# @Date:   2019-05-16T10:16:28+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-16T10:29:12+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

from keras import backend as K
from keras.engine.topology import Layer
from keras import initializers
from keras import models
import numpy as np

class Dozat(Layer):

    def __init__(self, a, b, output_dim, **kwargs):
        self.output_dim = output_dim
        super(Dozat, self).__init__(**kwargs)

    def call(self, x):
        m = K.random_uniform_variable((128, 128), 0, 1, seed=1)
        x = K.dot(a, m)
        x = K.batch_dot(x, b)
        x = K.argmax(x, axis=-1)
        return x

    def compute_output_shape(self, input_shape):
        return (shape_a[0], self.output_dim)











if __name__ == '__main__':
    print('hello, world~!')

## endl
