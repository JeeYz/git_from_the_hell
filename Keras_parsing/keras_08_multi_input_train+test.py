# @Author: J.Y.
# @Date:   2019-04-18T15:19:10+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-09-06T10:46:05+09:00
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

BATCH_SIZE = 128
EPOCHS = 10
W_VEC_SIZE = 128
P_VEC_SIZE = 128
INPUT_SIZE = (18*W_VEC_SIZE*2 + 18*P_VEC_SIZE*2)

fpath2 = 'd:/Program_Data/Parsing_Data/'
filewrite = '02_result_training.result'
savepara_name = 'd:/Program_Data/model_weights_k_25_chen_manning_Dropout.h5'

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

w_t = Input(batch_shape=(None, 36), dtype='int32', name='words')
p_t = Input(batch_shape=(None, 36), dtype='int32', name='pos')

ew1 = embedding_layer1(w)
ep1 = embedding_layer2(p)

ew1_t = embedding_layer1(w_t)
ep1_t = embedding_layer2(p_t)

embedded_sequences = layers.concatenate([ew1, ep1], axis=-1)
embedded_sequences = Flatten()(embedded_sequences)
embedded_sequences = Dropout(0.4)(embedded_sequences)
x = layers.Dense(512, activation='relu')(embedded_sequences)
x = Dropout(0.4)(x)
output_layer = layers.Dense(3, activation='softmax')(x)

embedded_sequences_t = layers.concatenate([ew1_t, ep1_t], axis=-1)
embedded_sequences_t = Flatten()(embedded_sequences_t)
x_t = layers.Dense(512, activation='relu')(embedded_sequences_t)
output_layer_t = layers.Dense(3, activation='softmax')(x_t)

network = Model([w, p], output_layer)
network_t = Model([w_t, p_t], output_layer_t)

network.summary()
network_t.summary()

# network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

correct = 0
total_q = 0
num = 0
network.save_weights(savepara_name, overwrite=True)

for i in range(EPOCHS):
    network.load_weights(savepara_name)
    for k,j in enumerate(filelist):
        network.load_weights(savepara_name)

        filename1 = fpath2 + j
        print('%d th epoch : ' %(i+1), filename1)
        word_data, pos_data, train_labels = k3.generate_train_data_3(filename1)
        network.fit({'words':word_data, 'pos':pos_data}, train_labels, epochs=5, batch_size=BATCH_SIZE)

        network.save_weights(savepara_name, overwrite=True)

    network_t.load_weights(savepara_name)

    for m,n in enumerate(all_sents):
        condition = 1
        action_stack = p0.make_dependency_tree(n)
        stack, buffer = p0.make_stack_buffer_list(n)
        a = all_init_test[m][0]
        b = all_init_test[m][1]
        # init_result = network.predict({'words':a, 'pos':b})
        init_result = network_t.predict({'words':a, 'pos':b})
        act = p0.select_action(init_result)
        while True:
            data, condition, stack, buffer, action_stack = p1.generate_data_of_test(act, stack,
                                                                buffer, w_dict, p_dict,
                                                                sent_Words_data[m], action_stack)
            if condition == 0:
                break

            a = data[0]
            b = data[1]
            if len(a[0]) != 36:
                print(a, len(a[0]))
            if len(b[0]) != 36:
                print(b, len(b[0]))
            a = np.array(a)
            b = np.array(b)
            # result = network.predict({'words':a, 'pos':b})
            result = network_t.predict({'words':a, 'pos':b})
            act = p0.select_action(result)
            if buffer == [] and len(stack) == 2:
                break

        parsing_table = p1.make_parsing_table(action_stack)
        a, b = p1.evaluate_result(parsing_table, sent_Words_data[m])
        correct += a
        total_q += b
        num += 1
    fw1 = open(fpath2 + filewrite, 'a', encoding='utf-8')
    print(correct, total_q, '\t%d th accuracy : %.3f %%' %(i, correct/total_q*100))
    fw1.write(str(correct) + str(total_q) + '\t%d th accuracy : %.3f %%' %(i, correct/total_q*100) + '\n')
    fw1.close()









## endl
