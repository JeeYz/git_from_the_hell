# @Author: J.Y.
# @Date:   2019-03-28T11:03:33+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-02T15:46:35+09:00
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
from keras.layers import Input, Dense
from keras.models import Model, Sequential
from keras import Input
from keras.initializers import Constant

import keras_module_0 as k0
import keras_module_1 as k1
import keras_module_2 as k2
import keras_module_3 as k3


BATCH_SIZE = 128
EPOCHS = 10
W_VEC_SIZE = 128
P_VEC_SIZE = 73
INPUT_SIZE = (18*W_VEC_SIZE*2 + 18*P_VEC_SIZE*2)

fpath2 = 'd:/Program_Data/Parsing_Data/'
filewrite = '00_result_training.result'

filelist = k1.generate_file_list(fpath2, '.train')
words_matrix = k3.make_word_list()
pos_matrix = k3.make_pos_list()

input_layer = Input(shape=(INPUT_SIZE, ), dtype = 'int32')

w1 = Input(shape=(None,), dtype='int32')
w2 = Input(shape=(None,), dtype='int32')
w3 = Input(shape=(None,), dtype='int32')
w4 = Input(shape=(None,), dtype='int32')
w5 = Input(shape=(None,), dtype='int32')
w6 = Input(shape=(None,), dtype='int32')
w7 = Input(shape=(None,), dtype='int32')
w8 = Input(shape=(None,), dtype='int32')
w9 = Input(shape=(None,), dtype='int32')
w10 = Input(shape=(None,), dtype='int32')
w11 = Input(shape=(None,), dtype='int32')
w12 = Input(shape=(None,), dtype='int32')
w13 = Input(shape=(None,), dtype='int32')
w14 = Input(shape=(None,), dtype='int32')
w15 = Input(shape=(None,), dtype='int32')
w16 = Input(shape=(None,), dtype='int32')
w17 = Input(shape=(None,), dtype='int32')
w18 = Input(shape=(None,), dtype='int32')
w19 = Input(shape=(None,), dtype='int32')
w20 = Input(shape=(None,), dtype='int32')
w21 = Input(shape=(None,), dtype='int32')
w22 = Input(shape=(None,), dtype='int32')
w23 = Input(shape=(None,), dtype='int32')
w24 = Input(shape=(None,), dtype='int32')
w25 = Input(shape=(None,), dtype='int32')
w26 = Input(shape=(None,), dtype='int32')
w27 = Input(shape=(None,), dtype='int32')
w28 = Input(shape=(None,), dtype='int32')
w29 = Input(shape=(None,), dtype='int32')
w30 = Input(shape=(None,), dtype='int32')
w31 = Input(shape=(None,), dtype='int32')
w32 = Input(shape=(None,), dtype='int32')
w33 = Input(shape=(None,), dtype='int32')
w34 = Input(shape=(None,), dtype='int32')
w35 = Input(shape=(None,), dtype='int32')
w36 = Input(shape=(None,), dtype='int32')

ew1 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w1)
ew2 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w2)
ew3 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w3)
ew4 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w4)
ew5 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w5)
ew6 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w6)
ew7 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w7)
ew8 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w8)
ew9 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w9)
ew10 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w10)
ew11 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w11)
ew12 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w12)
ew13 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w13)
ew14 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w14)
ew15 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w15)
ew16 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w16)
ew17 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w17)
ew18 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w18)
ew19 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w19)
ew20 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w20)
ew21 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w21)
ew22 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w22)
ew23 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w23)
ew24 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w24)
ew25 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w25)
ew26 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w26)
ew27 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w27)
ew28 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w28)
ew29 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w29)
ew30 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w30)
ew31 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w31)
ew32 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w32)
ew33 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w33)
ew34 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w34)
ew35 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w35)
ew36 = layers.Embedding(len(words_matrix), W_VEC_SIZE, embeddings_initializer=Constant(words_matrix))(w36)

embedded_sequences = layers.concatenate([ew1, ew2, ew3, ew4, ew5, ew6, ew7, ew8, ew9, ew10, ew11, ew12,ew13, ew14, ew15, ew16, ew17, ew18, ew19, ew20, ew21, ew22, ew23, ew24, ew25, ew26, ew27, ew28, ew29, ew30, ew31, ew32, ew33, ew34, ew35, ew36], axis=-1)
x = layers.Dense(512, activation='relu')(embedded_sequences)
output_layer = layers.Dense(3, activation='softmax')(x)

network = Model([w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19, w20, w21, w22, w23, w24, w25, w26, w27, w28, w29, w30, w31, w32, w33, w34, w35, w36], output_layer)
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
        [word_data, pos_data], train_labels = k3.generate_train_data_3(filename1)
        network.fit([word_data, pos_data], train_labels, epochs=15, batch_size=BATCH_SIZE)
        network.save_weights('d:/Program_Data/model_weights_k_3.h5', overwrite=True)
        # print('+++++++++++++++++++++++++++++++++')
        # print(network.get_weights())
        # print('+++++++++++++++++++++++++++++++++\n\n')











## endl
