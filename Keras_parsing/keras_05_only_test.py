# @Author: J.Y.
# @Date:   2019-03-21T15:47:00+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-27T14:26:20+09:00
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

batch_size = 128
epochs = 3
w_vec_size = 128
p_vec_size = 73
input_size = (18*w_vec_size*2 + 18*p_vec_size*2)

fpath1 = 'd:/Program_Data/'
fpath2 = 'd:/Program_Data/Parsing_Data/'
filename1 = fpath1 + 'raw_test_dataset_05.test'
filewrite = fpath2 + '00_result_training.result'

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(input_size, )))
network.add(layers.Dense(3, activation='softmax'))
# network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

## 10 * 3 epoch trained weights parameter
network.load_weights('d:/Program_Data/model_weights_k_1.h5', overwrite=True)

## test session
with open(filename1, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:break












## endl
