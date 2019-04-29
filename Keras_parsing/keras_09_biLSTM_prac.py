# @Author: J.Y.
# @Date:   2019-04-25T10:56:41+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-29T09:43:33+09:00
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

import keras_module_0 as k0
import keras_module_1 as k1
import keras_module_2 as k2
import keras_module_3 as k3
import keras_module_for_fastText as kfT

import parsing_module_0 as p0
import parsing_module_1 as p1
import parsing_module_2 as p2

BATCH_SIZE = 128
EPOCHS = 10
W_VEC_SIZE = 128
P_VEC_SIZE = 128
INPUT_SIZE = (18*W_VEC_SIZE*2 + 18*P_VEC_SIZE*2)

fpath2 = 'd:/Program_Data/Parsing_Data/'
filewrite = '00_result_training.result'
savepara_name = 'd:/Program_Data/model_weights_k_16_dim_128_fT_pos_128dim_Dropout.h5'

# fw1 = open(fpath2 + filewrite, 'a', encoding='utf-8')
filelist = k1.generate_file_list(fpath2, '.train')
# words_matrix = k3.make_word_list(W_VEC_SIZE)
# pos_matrix = k3.make_pos_list(P_VEC_SIZE)
words_matrix = kfT.words_matrix_fastText(W_VEC_SIZE)
pos_matrix = kfT.make_pos_fastText(P_VEC_SIZE)

all_sents, sent_Words_data = p0.make_all_sents_to_list()
all_init_test = p0.make_all_init_test_data()
w_dict, p_dict = p0.make_words_pos_dict()

embedding_layer1 = Embedding(len(words_matrix), W_VEC_SIZE,
                            embeddings_initializer=Constant(words_matrix),
                            input_length=36)
embedding_layer2 = Embedding(len(pos_matrix), P_VEC_SIZE,
                            embeddings_initializer=Constant(pos_matrix),
                            input_length=36)

w = Input(batch_shape=(None, 36), dtype='int32', name='words')
p = Input(batch_shape=(None, 36), dtype='int32', name='pos')

ew1 = embedding_layer1(w)
ep1 = embedding_layer2(p)

embedded_sequences = layers.concatenate([ew1, ep1], axis=-1)
embedded_sequences = Flatten()(embedded_sequences)

x = Bidirectional(LSTM(128, return_sequences=True, dropout=0.15, recurrent_dropout=0.15))(x)
x = Dropout(0.4)(x)
a = layers.Dense(512, activation='relu')(x)
b = layers.Dense(512, activation='relu')(x)

a = p2.make_matrix_A(a)
b = p2.make_matrix_A(b)
b = backend.permute_dimensions(b, (0, 2, 1))

x = layers.Dense((W_VEC_SIZE+1)*W_VEC_SIZE)(a)
x = Multiply([x, b])





embedded_sequences = Dropout(0.4)(embedded_sequences)
x = layers.Dense(512, activation='relu')(embedded_sequences)
x = Dropout(0.4)(x)
output_layer = layers.Dense(3, activation='softmax')(x)

network = Model([w, p], output_layer)
network.summary()

# network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
network.save_weights(savepara_name, overwrite=True)

correct = 0
total_q = 0
num = 0














## endl
