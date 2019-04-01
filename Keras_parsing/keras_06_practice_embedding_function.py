# @Author: J.Y.
# @Date:   2019-03-28T11:03:33+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-01T17:51:47+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

from __future__ import print_function

import os
import sys
import numpy as np

from keras import models
from keras import layers
from keras.models import load_model
from keras.layers import Input, Dense
from keras.models import Model, Sequential
from keras import Input

import keras_module_0 as k0
import keras_module_1 as k1
import keras_module_2 as k2
import keras_module_3 as k3


BATCH_SIZE = 128
EPOCHS = 10
W_VEC_SIZE = 128
P_VEC_SIZE = 73
INPUT_SIZE = (18*W_VEC_SIZE*2 + 18*P_VEC_SIZE*2)
MAX_SEQUENCE_LENGTH = 36

fpath2 = 'd:/Program_Data/Parsing_Data/'
filewrite = '00_result_training.result'

filelist = k1.generate_file_list(fpath2, '.train')
# testlist = k1.generate_file_list(fpath2, '.test')
words_matrix = k3.make_word_list()
pos_matrix = k3.make_pos_list()

embedding_layer1 = Embedding(len(words_matrix)+1,
                            W_VEC_SIZE,
                            embeddings_initializer=Constant(words_matrix),
                            input_length=MAX_SEQUENCE_LENGTH,
                            trainable=False)

embedding_layer2 = Embedding(P_VEC_SIZE,
                            P_VEC_SIZE,
                            embeddings_initializer=Constant(pos_matrix),
                            input_length=MAX_SEQUENCE_LENGTH,
                            trainable=False)

# network = models.Sequential()
input_layer = Input(shape=(INPUT_SIZE, ), dtype = 'int32')
sequence_input1 = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')
sequence_input2 = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')
# embedded_sequences = embedding_layer1(sequence_input1) + embedding_layer2(sequence_input2)
embedded_sequences = layers.concatenate([sequence_input1, sequence_input2], axis=-1)
# network.add(layers.Dense(512, activation='relu', input_shape=(INPUT_SIZE, )))
# network.add(layers.Dense(3, activation='softmax'))
x = layers.Dense(512, activation='relu')(embedded_sequences)
output_layer = layers.Dense(3, activation='softmax')(x)

network = Model(input_layer, output_layer)
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
        train_data, train_labels = k3.generate_train_data_3(filename1)
        network.fit(train_data, train_labels, epochs=15, batch_size=BATCH_SIZE)
        network.save_weights('d:/Program_Data/model_weights_k_3.h5', overwrite=True)
        # print('+++++++++++++++++++++++++++++++++')
        # print(network.get_weights())
        # print('+++++++++++++++++++++++++++++++++\n\n')











## endl
