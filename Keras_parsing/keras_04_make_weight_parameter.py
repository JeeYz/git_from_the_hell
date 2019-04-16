# @Author: J.Y.
# @Date:   2019-03-21T15:47:00+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-15T15:43:03+09:00
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
import keras_module_for_fastText as kfT

batch_size = 128
epochs = 1
w_vec_size = 128
p_vec_size = 73
input_size = (18*w_vec_size*2 + 18*p_vec_size*2)
train_limit = 100
test_limit = 100

fpath2 = 'd:/Program_Data/Parsing_Data/'
filewrite = '00_result_training.result'
savepara_name = 'd:/Program_Data/model_weights_k_8_vec_dim_128_rand_not_update.h5'

filelist = k1.generate_file_list(fpath2, '.train')
# testlist = k1.generate_file_list(fpath2, '.test')
words_matrix = k0.make_word_list(w_vec_size)
pos_matrix = k0.make_pos_list()


network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(input_size, )))
network.add(layers.Dense(3, activation='softmax'))
# network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
network.save_weights(savepara_name, overwrite=True)

for i in range(epochs):
    for k,j in enumerate(filelist):
        network.load_weights(savepara_name)

        filename1 = fpath2 + j
        print('%d th epoch : ' %(i+1), filename1)

        train_data, train_labels = k0.generate_train_data_2(filename1, words_matrix, pos_matrix)

        network.fit(train_data, train_labels, epochs=10, batch_size=batch_size)
        network.save_weights(savepara_name, overwrite=True)







## endl
