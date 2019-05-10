# @Author: J.Y.
# @Date:   2019-05-09T11:28:21+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-05-10T13:04:24+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

from __future__ import print_function

import os
import sys
import numpy as np
sys.path.append(r'./module')

from keras import models
from keras import layers
from keras import backend
from keras.models import load_model
from keras.layers import Input, Dense, Embedding, Flatten, Dropout
from keras.layers import LSTM, Bidirectional, Multiply
from keras.models import Model, Sequential
from keras import Input
from keras.initializers import Constant

import keras_module_for_fastText as kfT

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

word, pos, label = p3.make_small_train_data()

w = Input(shape=(None, 2), dtype='int32', name='words')
p = Input(shape=(None, 2), dtype='int32', name='pos')
l = Input(shape=(None, 1), dtype='int32', name='length')

print(w, p, l)
print(backend.int_shape(w))
print(backend.int_shape(l))
print(backend.eval(l))

embedding_layer1 = Embedding(len(words_matrix), W_VEC_SIZE,
                            embeddings_initializer=Constant(words_matrix))
embedding_layer2 = Embedding(len(pos_matrix), P_VEC_SIZE,
                            embeddings_initializer=Constant(pos_matrix))

ew1 = embedding_layer1(w)
ep1 = embedding_layer2(p)
# print(backend.shape(w))
# length = len(w)
# print(length)
print(ew1, ep1)
ew1 = Flatten()(ew1)
ep1 = Flatten()(ep1)
print(ew1, ep1)
es = layers.concatenate([ew1, ep1], axis=-1) ## es = embedded_sequences
print(es)

x = Bidirectional(LSTM(128, return_sequences=True,
                    input_shape=(1, length, 512)), merge_mode='concat')(es)

print(x)
x = Dropout(0.4)(x)
a = layers.Dense(512, activation='relu')(x)
b = layers.Dense(512, activation='relu')(x)

b = backend.permute_dimensions(b, (0, 2, 1))

x = layers.Dense((W_VEC_SIZE+1)*W_VEC_SIZE)(a)
output_matrix = Multiply([x, b])
result_matrix = p2.make_softmax(output_matrix)

network = Model([w, p], output_layer)
network.summary()

# network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
network.save_weights(savepara_name, overwrite=True)

correct = 0
total_q = 0
num = 0
for i in range(EPOCHS):
    network.load_weights(savepara_name)
    network.fit({'words':word, 'pos':pos, 'length':len(word)}, label,
                    epochs=5, batch_size=1)
    network.save_weights(savepara_name, overwrite=True)











## endl
