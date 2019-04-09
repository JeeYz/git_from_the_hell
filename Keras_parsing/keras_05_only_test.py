# @Author: J.Y.
# @Date:   2019-03-21T15:47:00+09:00
# @Project: NLP
# @Last modified by:   J.Y.
<<<<<<< HEAD
# @Last modified time: 2019-04-09T16:45:30+09:00
=======
# @Last modified time: 2019-04-09T16:45:30+09:00
>>>>>>> f3c7853cbd3358971ab65c68bd55224ae1e1b0d8
# @License: JeeY
# @Copyright: J.Y. JeeY

import os
import sys
import datetime
sys.path.append(r'./module')
import numpy as np

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

import parsing_module_0 as p0
import parsing_module_1 as p1

import h5py
filename = 'd:/Program_Data/model_weights_k_3.h5'
f = h5py.File(filename, 'r')

BATCH_SIZE = 128
EPOCHS = 1
W_VEC_SIZE = 128
P_VEC_SIZE = 73
INPUT_SIZE = (18*W_VEC_SIZE*2 + 18*P_VEC_SIZE*2)

fpath2 = 'd:/Program_Data/Parsing_Data/'
filewrite = '00_result_training.result'

filelist = k1.generate_file_list(fpath2, '.train')
all_sents, sent_Words_data = p0.make_all_sents_to_list()
all_init_test = p0.make_all_init_test_data()
w_dict, p_dict = p0.make_words_pos_dict()

embedding_layer1 = Embedding(len(words_matrix), W_VEC_SIZE)
embedding_layer2 = Embedding(P_VEC_SIZE, P_VEC_SIZE)

w = Input(shape=(36, ), dtype='int32', name='words')
p = Input(shape=(36, ), dtype='int32', name='pos')

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
network.load_weights('d:/Program_Data/model_weights_k_3.h5')

## test session
for i,j in enumerate(all_sents):
    action_stack = p0.make_dependency_tree(j)
    stack, buffer = p0.make_stack_buffer_list(j)
    a = all_init_test[i][0]
    b = all_init_test[i][1]
    init_result = network.predict({'words':a, 'pos':b})
    act = p0.select_action(init_result)
    while True:
        data = p1.generate_data_of_test(act, stack, buffer, w_dict, p_dict, sent_Words_data[i], action_stack)
        a = data[0]
        b = data[1]
        result = network.predict({'words':a, 'pos':b})
        act = p0.select_action(result)
        if buffer == [] and len(stack) == 2:
            break












## endl
