# @Author: J.Y.
# @Date:   2019-03-28T11:03:33+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-15T11:05:06+09:00
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
from keras.layers import Input, Dense, Embedding, Flatten
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
# filewrite = '00_result_training.result'
savepara_name = 'd:/Program_Data/model_weights_k_6_vec_dim_300.h5'

filelist = k1.generate_file_list(fpath2, '.train')
words_matrix = k3.make_word_list()
pos_matrix = k3.make_pos_list()

embedding_layer1 = Embedding(len(words_matrix), W_VEC_SIZE,
                            embeddings_initializer=Constant(words_matrix),
                            input_length=36)
embedding_layer2 = Embedding(P_VEC_SIZE, P_VEC_SIZE,
                            embeddings_initializer=Constant(pos_matrix),
                            input_length=36)

w = Input(batch_shape=(None, 36), dtype='int32', name='words')
p = Input(batch_shape=(None, 36), dtype='int32', name='pos')

ew1 = embedding_layer1(w)
ep1 = embedding_layer2(p)
embedded_sequences = layers.concatenate([ew1, ep1], axis=-1)
embedded_sequences = Flatten()(embedded_sequences)
x = layers.Dense(512, activation='relu')(embedded_sequences)
output_layer = layers.Dense(3, activation='softmax')(x)

network = Model([w, p], output_layer)
network.summary()

# network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
network.save_weights(savepara_name, overwrite=True)

for i in range(EPOCHS):
    for k,j in enumerate(filelist):
        network.load_weights(savepara_name)
        # print('*****************************')
        # print(network.get_weights())
        # print('*****************************\n\n')
        filename1 = fpath2 + j
        print('%d th epoch : ' %(i+1), filename1)
        word_data, pos_data, train_labels = k3.generate_train_data_3(filename1)
        network.fit({'words':word_data, 'pos':pos_data}, train_labels, epochs=5, batch_size=BATCH_SIZE)
        # result = network.predict({'words':word_data, 'pos':pos_data})
        # print(result)
        network.save_weights(savepara_name, overwrite=True)
        # print('+++++++++++++++++++++++++++++++++')
        # print(network.get_weights())
        # print('+++++++++++++++++++++++++++++++++\n\n')











## endl
