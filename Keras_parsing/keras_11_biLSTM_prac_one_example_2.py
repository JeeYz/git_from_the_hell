# @Author: J.Y.
# @Date:   2019-05-09T11:28:21+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-22T16:25:05+09:00
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

word_all, pos_all, label_all = p3.make_train_data()
print('data loaded complete~!!')

w = Input(shape=(None, 2), dtype='int32', name='words')
p = Input(shape=(None, 2), dtype='int32', name='pos')
# w = Input(batch_shape=(None, None, 2), dtype='int32', name='words')
# p = Input(batch_shape=(None, None, 2), dtype='int32', name='pos')

embedding_layer1 = Embedding(len(words_matrix), W_VEC_SIZE,
                            embeddings_initializer=Constant(words_matrix))
embedding_layer2 = Embedding(len(pos_matrix), P_VEC_SIZE,
                            embeddings_initializer=Constant(pos_matrix))

ew1 = embedding_layer1(w)
ep1 = embedding_layer2(p)

# ew1 = backend.reshape(ew1, shape=(1, -1, W_VEC_SIZE*2))
# ep1 = backend.reshape(ep1, shape=(1, -1, P_VEC_SIZE*2))
ew1 = Reshape((-1, W_VEC_SIZE*2))(ew1)
ep1 = Reshape((-1, P_VEC_SIZE*2))(ep1)
# print(ew1, ep1, '\n\n\n')
es = layers.concatenate([ew1, ep1], axis=-1) ## es = embedded_sequences

x = Bidirectional(LSTM(128, return_sequences=True,
                    input_shape=(1, None, 512)), merge_mode='concat')(es)

x = Dozat(None)(x) # custom Lambda layer

network = Model([w, p], x)

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
    for i,j in enumerate(word_all):
        # print(word_all[i])
        word = np.array([word_all[i]])
        pos = np.array([pos_all[i]])
        label = np.array([label_all[i]])
        network.fit({'words':word, 'pos':pos}, label,
                        epochs=1, batch_size=1)
    # word_all = np.array(word_all)
    # pos_all = np.array(pos_all)
    # label_all = np.array(label_all)
    # network.fit({'words':word_all, 'pos':pos_all}, label_all,
    #                 epochs=5, batch_size=128)
    network.save_weights(savepara_name, overwrite=True)













## endl
