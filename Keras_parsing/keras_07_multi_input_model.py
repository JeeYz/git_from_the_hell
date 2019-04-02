# @Author: J.Y.
# @Date:   2019-03-28T11:03:33+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-02T17:22:57+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

from __future__ import print_function

import os
import sys
import numpy as np
sys.path.append(r'./module')

from keras import models
from keras import layers
from keras.models import load_model
from keras.layers import Input, Dense, Embedding
from keras.models import Model, Sequential
from keras import Input
from keras.initializers import Constant

import keras_module_0 as k0
import keras_module_1 as k1
import keras_module_2 as k2
import keras_module_3 as k3


BATCH_SIZE = 128
EPOCHS = 1
W_VEC_SIZE = 128
P_VEC_SIZE = 73
INPUT_SIZE = (18*W_VEC_SIZE*2 + 18*P_VEC_SIZE*2)

fpath2 = 'd:/Program_Data/Parsing_Data/'
filewrite = '00_result_training.result'

filelist = k1.generate_file_list(fpath2, '.train')
words_matrix = k3.make_word_list()
pos_matrix = k3.make_pos_list()

w = Input(shape=(36,), dtype='int32', name='words')
p = Input(shape=(36,), dtype='int32', name='pos')

embedding_layer1 = Embedding(len(words_matrix), W_VEC_SIZE,
                            embeddings_initializer=Constant(words_matrix),
                            input_length=36)
embedding_layer2 = Embedding(P_VEC_SIZE, P_VEC_SIZE,
                            embeddings_initializer=Constant(pos_matrix),
                            input_length=36)

ew1 = embedding_layer1(w)
ep1 = embedding_layer2(p)

embedded_sequences = layers.concatenate([ew1, ep1], axis=-1)
x = layers.Dense(512, activation='relu')(embedded_sequences)
output_layer = layers.Dense(3, activation='softmax')(x)

network = Model([w, p], output_layer)
network.summary()

# network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
network.save_weights('d:/Program_Data/model_weights_k_3.h5', overwrite=True)

for i in range(EPOCHS):
    for k,j in enumerate(filelist):
        network.load_weights('d:/Program_Data/model_weights_k_3.h5')
        # print('*****************************')
        # print(network.get_weights())
        # print('*****************************\n\n')
        filename1 = fpath2 + j
        print('%d th epoch : ' %(i+1), filename1)
        word_data, pos_data, train_labels = k3.generate_train_data_3(filename1)
        network.fit({'words':word_data, 'pos':pos_data}, train_labels, epochs=15, batch_size=BATCH_SIZE)
        network.save_weights('d:/Program_Data/model_weights_k_3.h5', overwrite=True)
        # print('+++++++++++++++++++++++++++++++++')
        # print(network.get_weights())
        # print('+++++++++++++++++++++++++++++++++\n\n')











## endl
