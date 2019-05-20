# @Author: J.Y.
# @Date:   2019-05-09T11:28:21+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-20T16:45:38+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

from __future__ import print_function

import os
import sys
import numpy as np
import tensorflow as tf
sys.path.append(r'./module')

from keras import models
from keras import layers
from keras import backend
from keras import activations
from keras.activations import softmax
from keras.models import load_model
from keras.layers import Input, Dense, Embedding, Flatten, Dropout
from keras.layers import LSTM, Bidirectional, Multiply, Reshape, Lambda
from keras.models import Model, Sequential
from keras import Input
from keras.initializers import Constant
from keras.backend import argmax
from custom_layer_0 import Dozat

import keras_module_for_fastText as kfT

import parsing_module_2 as p2
import parsing_module_3 as p3

from parsing_module_3 import find_argmax

BATCH_SIZE = 128
EPOCHS = 10
W_VEC_SIZE = 128
P_VEC_SIZE = 128
INPUT_SIZE = (18*W_VEC_SIZE*2 + 18*P_VEC_SIZE*2)

fpath2 = 'd:/Program_Data/Parsing_Data/'
filewrite = '00_result_training.result'
trainfile = 'd:/Program_Data/raw_train_dataset_23.train'
savepara_name = 'd:/Program_Data/model_weights_k_17_bi_LSTM_proto.h5'

words_matrix = kfT.words_matrix_fastText(W_VEC_SIZE)
pos_matrix = kfT.make_pos_fastText(P_VEC_SIZE)

word, pos, label = p3.make_small_train_data()

w = Input(shape=(21, 2), dtype='int32', name='words')
p = Input(shape=(21, 2), dtype='int32', name='pos')
# l = Input(shape=(None, 1), dtype='int32', name='length')
#
# print(w, p)
# print(backend.gather(w, 2))
# print('\n')
# print(backend.int_shape(w))
# # print(backend.print_tensor(w))
# print('\n\n\n')

embedding_layer1 = Embedding(len(words_matrix), W_VEC_SIZE,
                            embeddings_initializer=Constant(words_matrix))
embedding_layer2 = Embedding(len(pos_matrix), P_VEC_SIZE,
                            embeddings_initializer=Constant(pos_matrix))

ew1 = embedding_layer1(w)
ep1 = embedding_layer2(p)

# print(ew1, ep1, '\n\n\n')

# ew1 = backend.reshape(ew1, shape=(1, -1, W_VEC_SIZE*2))
# ep1 = backend.reshape(ep1, shape=(1, -1, P_VEC_SIZE*2))
ew1 = Reshape((-1, W_VEC_SIZE*2))(ew1)
ep1 = Reshape((-1, P_VEC_SIZE*2))(ep1)
# print(ew1, ep1, '\n\n\n')
es = layers.concatenate([ew1, ep1], axis=-1) ## es = embedded_sequences

# print(es, '\n\n\n')

x = Bidirectional(LSTM(128, return_sequences=True,
                    input_shape=(1, 21, 512)), merge_mode='concat')(es)

# print('x : ', backend.int_shape(x), x, '\n\n\n')

x = Dozat(21)(x) # custom Lambda layer

# print('x : ', x, '\n\n\n')

network = Model([w, p], x)
# q = network.layers[8].output
# print(q)

network.summary()

# network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
# network.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
network.save_weights(savepara_name, overwrite=True)

correct = 0
total_q = 0
num = 0
for i in range(EPOCHS):
    network.load_weights(savepara_name)
    network.fit({'words':word, 'pos':pos}, label,
                    epochs=5, batch_size=1)
    print(x)
    network.save_weights(savepara_name, overwrite=True)













## endl
