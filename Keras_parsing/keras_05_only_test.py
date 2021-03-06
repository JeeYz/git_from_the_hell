# @Author: J.Y.
# @Date:   2019-03-21T15:47:00+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-18T15:12:50+09:00
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
import keras_module_for_fastText as kfT

import parsing_module_0 as p0
import parsing_module_1 as p1

import h5py
# filename = 'd:/Program_Data/model_weights_k_4.h5'
# f = h5py.File(filename, 'r')

BATCH_SIZE = 128
EPOCHS = 1
W_VEC_SIZE = 128
P_VEC_SIZE = 128
INPUT_SIZE = (18*W_VEC_SIZE*2 + 18*P_VEC_SIZE*2)

fpath2 = 'd:/Program_Data/Parsing_Data/'
filewrite = '00_result_training.result'

savepara_name = 'd:/Program_Data/model_weights_k_14_dim_128_fT_pos_128dim.h5'

filelist = k1.generate_file_list(fpath2, '.train')
words_matrix = kfT.words_matrix_fastText(W_VEC_SIZE)
# words_matrix = k3.make_word_list(W_VEC_SIZE)
pos_matrix = k3.make_pos_list(P_VEC_SIZE)
all_sents, sent_Words_data = p0.make_all_sents_to_list()
all_init_test = p0.make_all_init_test_data()
w_dict, p_dict = p0.make_words_pos_dict()

embedding_layer1 = Embedding(len(words_matrix), W_VEC_SIZE)
embedding_layer2 = Embedding(len(pos_matrix), P_VEC_SIZE)

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
network.load_weights(savepara_name)

## test session
correct = 0
total_q = 0
num = 0
for i,j in enumerate(all_sents):
    condition = 1
    action_stack = p0.make_dependency_tree(j)
    stack, buffer = p0.make_stack_buffer_list(j)
    a = all_init_test[i][0]
    b = all_init_test[i][1]
    init_result = network.predict({'words':a, 'pos':b})
    act = p0.select_action(init_result)
    # print('\n')
    # print('ACTION : ', act)
    # print('\n')
    while True:
        data, condition, stack, buffer, action_stack = p1.generate_data_of_test(act, stack,
                                                            buffer, w_dict, p_dict,
                                                            sent_Words_data[i], action_stack)
        if condition == 0:
            break
        # print(data)
        # print(len(data[0][0]), len(data[1][0]))
        a = data[0]
        b = data[1]
        if len(a[0]) != 36:
            print(a, len(a[0]))
        if len(b[0]) != 36:
            print(b, len(b[0]))
        a = np.array(a)
        b = np.array(b)
        result = network.predict({'words':a, 'pos':b})
        act = p0.select_action(result)
        # print('\n')
        # print('ACTION : ', act)
        # print('\n')
        if buffer == [] and len(stack) == 2:
            break

    parsing_table = p1.make_parsing_table(action_stack)
    # print(parsing_table)
    a, b = p1.evaluate_result(parsing_table, sent_Words_data[i])
    correct += a
    total_q += b
    num += 1
    if num%100 == 0:
        print(correct, total_q, '\taccuracy : %.3f %%' % (correct/total_q*100))











## endl
