# @Author: J.Y.
# @Date:   2019-04-25T10:56:41+09:00
# @Project: NLP
# @Last modified by:   J.Y.
<<<<<<< HEAD
# @Last modified time: 2019-04-30T16:38:30+09:00
=======
# @Last modified time: 2019-04-30T16:38:30+09:00
>>>>>>> 30b1d1b8ebe8b94538fab7853500cc1cafe97cfa
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
trainfile = 'd:/Program_Data/raw_train_dataset_21.train'
savepara_name = 'd:/Program_Data/model_weights_k_17_bi_LSTM_proto.h5'

# words_matrix = k3.make_word_list(W_VEC_SIZE)
# pos_matrix = k3.make_pos_list(P_VEC_SIZE)
words_matrix = kfT.words_matrix_fastText(W_VEC_SIZE)
pos_matrix = kfT.make_pos_fastText(P_VEC_SIZE)

all_word, all_pos = p2.make_all_data()
all_label, all_sent = p2.make_label_matrix()
# all_init_test = p0.make_all_init_test_data()
# w_dict, p_dict = p0.make_words_pos_dict()

embedding_layer1 = Embedding(len(words_matrix), W_VEC_SIZE,
                            embeddings_initializer=Constant(words_matrix),
                            input_length=36)
embedding_layer2 = Embedding(len(pos_matrix), P_VEC_SIZE,
                            embeddings_initializer=Constant(pos_matrix),
                            input_length=36)

w = Input(batch_shape=(None, 2), dtype='int32', name='words')
p = Input(batch_shape=(None, 2), dtype='int32', name='pos')
length = Input(batch_shape=(None, 1), dtype='int32', name='length')

ew1 = embedding_layer1(w)
ep1 = embedding_layer2(p)

embedded_sequences = layers.concatenate([ew1, ep1], axis=-1)
embedded_sequences = Flatten()(embedded_sequences)

x = Bidirectional(LSTM(length, return_sequences=True,
                    dropout=0.15, recurrent_dropout=0.15,
                    input_shape=(1, 512), BATCH_SIZE=1))(embedded_sequences)
x = Dropout(0.4)(x)
a = layers.Dense(512, activation='relu')(x)
b = layers.Dense(512, activation='relu')(x)

a = p2.make_matrix_A(a)
b = p2.make_matrix_A(b)
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
    for k,sent_words in enumerate(all_word):
        network.load_weights(savepara_name)
        filename1 = fpath2 + j
        print('%d th epoch : ' %(i+1), filename1)
        network.fit({'words':sent_words, 'pos':all_pos[k], 'length':len(all_sent[k])},
                        all_label[k], epochs=5)
        network.save_weights(savepara_name, overwrite=True)














## endl
