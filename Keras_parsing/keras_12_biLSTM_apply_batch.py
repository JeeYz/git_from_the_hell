# @Author: J.Y.
# @Date:   2019-05-09T11:28:21+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-09-05T18:45:55+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

from __future__ import print_function

import os
import sys
import numpy as np
import tensorflow as tf
import time
sys.path.append(r'./module')

from keras import models, layers, activations, Input
from keras import backend as K
from keras.activations import softmax
from keras.models import load_model
from keras.layers import Input, Dense, Embedding, Dropout
from keras.layers import LSTM, Bidirectional, Reshape, Lambda
from keras.models import Model, Sequential
from keras.initializers import Constant
from keras.backend import argmax
from custom_layer_0 import Dozat, Dozat_t

import keras_module_for_fastText as kfT

import keras_module_1 as k1
import parsing_module_2 as p2
import parsing_module_3 as p3
import parsing_module_4 as p4

BATCH_SIZE = 128
EPOCHS = 20
W_VEC_SIZE = 128
P_VEC_SIZE = 128
MAX_SENT_SIZE = 41
NUM_OF_CELLS = 128
INPUT_SIZE = (18*W_VEC_SIZE*2 + 18*P_VEC_SIZE*2)

fpath = 'd:/Program_Data/Parsing_Data_BiLSTM_batch/'
filewrite = '01_result_training_BiLSTM_batch.result'
savepara_name = 'd:/Program_Data/model_weights_k_24_BiLSTM_batch_00.h5'

filelist = k1.generate_file_list(fpath, '.train')

words_matrix = kfT.words_matrix_fastText(W_VEC_SIZE)
pos_matrix = kfT.make_pos_fastText(P_VEC_SIZE)

# word_all, pos_all, label_all = p3.make_train_data()
test_word, test_pos, test_label = p3.make_test_data()
# print('data loaded complete~!!')

w_t = Input(shape=(None, 2), dtype='int32', name='words')
p_t = Input(shape=(None, 2), dtype='int32', name='pos')
w = Input(batch_shape=(None, MAX_SENT_SIZE, 2), dtype='int32', name='words')
p = Input(batch_shape=(None, MAX_SENT_SIZE, 2), dtype='int32', name='pos')

embedding_layer1 = Embedding(len(words_matrix), W_VEC_SIZE,
                            embeddings_initializer=Constant(words_matrix))
embedding_layer2 = Embedding(len(pos_matrix), P_VEC_SIZE,
                            embeddings_initializer=Constant(pos_matrix))

ew1 = embedding_layer1(w)
ep1 = embedding_layer2(p)

ew1_t = embedding_layer1(w_t)
ep1_t = embedding_layer2(p_t)

# ew1 = backend.reshape(ew1, shape=(1, -1, W_VEC_SIZE*2))
# ep1 = backend.reshape(ep1, shape=(1, -1, P_VEC_SIZE*2))
ew1 = Reshape((-1, W_VEC_SIZE*2))(ew1)
ep1 = Reshape((-1, P_VEC_SIZE*2))(ep1)

ew1_t = Reshape((-1, W_VEC_SIZE*2))(ew1_t)
ep1_t = Reshape((-1, P_VEC_SIZE*2))(ep1_t)
# print(ew1, ep1, '\n\n\n')
es = layers.concatenate([ew1, ep1], axis=-1) ## es = embedded_sequences
es_t = layers.concatenate([ew1_t, ep1_t], axis=-1) ## es = embedded_sequences

x = Bidirectional(LSTM(NUM_OF_CELLS, return_sequences=True,
                    input_shape=(BATCH_SIZE, None, 512)), merge_mode='concat')(es)

x_t = Bidirectional(LSTM(NUM_OF_CELLS, return_sequences=True,
                    input_shape=(BATCH_SIZE, None, 512)), merge_mode='concat')(es_t)

x = Dozat(None)(x) # custom Lambda layer

x_t = Dozat_t(None)(x_t) # custom Lambda layer

network = Model([w, p], x)
network_t = Model([w_t, p_t], x_t)

network.summary()
network_t.summary()

# network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
# network.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
network.save_weights(savepara_name, overwrite=True)

# fw = open(fpath + filewrite, 'a', encoding='utf-8')

for l in range(EPOCHS):
    w_filename = fpath + filewrite
    network.load_weights(savepara_name)
    fw = open(w_filename, 'a', encoding='utf-8')

    for k,j in enumerate(filelist):
        filename = fpath + j
        print('%d th epoch : ' %(l+1), filename)
        word, pos, label = p4.make_train_data(filename)

        # print(word)
        # print(word.shape)
        # print(word[0][0][0])
        # time.sleep(10000)

        network.fit({'words':word, 'pos':pos}, label, epochs=1, batch_size=BATCH_SIZE)
        network.save_weights(savepara_name, overwrite=True)

    total_correct = 0
    total_num = 0

    for m,n in enumerate(test_word):
        word = np.array([test_word[m]])
        pos = np.array([test_pos[m]])
        label = np.array([test_label[m]])
        test_result = network_t.predict({'words':word, 'pos':pos})
        # print(test_result)
        # test_result = np.array(test_result)
        # print(test_result)
        # print(label)
        a, b = p3.evaluate_result(test_result, label)
        total_correct += a
        total_num += b
        # print(total_correct, total_num)
    print(total_correct, total_num)
    print('\n\n\n')
    fw.write('\n\n\n')
    print(total_correct/total_num)
    fw.write(str(total_correct/total_num) + '\n')
    print('\n\n\n')
    fw.write('\n\n\n')
    network.save_weights(savepara_name, overwrite=True)
    fw.close()



# fw.close()





















## endl
