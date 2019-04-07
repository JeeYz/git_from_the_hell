# @Author: J.Y.
# @Date:   2019-03-21T15:47:00+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-08T05:26:31+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import os
import sys
import datetime
sys.path.append(r'./module')

from keras import models
from keras import layers
from keras.models import load_model
from keras.layers import Input, Dense
from keras.models import Model, Sequential

import keras_module_0 as k0
import keras_module_1 as k1
import keras_module_2 as k2
import keras_module_3 as k3

import parsing_module_0 as p0

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
all_sents = p0.make_all_sents_to_list()
all_init_test = p0.

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
network.load_weights('d:/Program_Data/model_weights_k_3.h5', overwrite=True)

## test session
for i,j in enumerate(all_sents):
    stack, buffer = p0.make_stack_buffer_list(i)
    condition = 1
    while True:
        if condition == 0:break
        network.predict()












## endl
