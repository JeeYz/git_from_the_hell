# @Author: J.Y.
# @Date:   2019-03-21T15:47:00+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-26T17:08:06+09:00
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

batch_size = 128
epochs = 10
w_vec_size = 128
p_vec_size = 73
input_size = (18*w_vec_size*2 + 18*p_vec_size*2)
train_limit = 100
test_limit = 100

fpath2 = 'd:/Program_Data/Parsing_Data/'
filewrite = '00_result_training.result'

filelist = k1.generate_file_list(fpath2, '.train')
# testlist = k1.generate_file_list(fpath2, '.test')

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(input_size, )))
network.add(layers.Dense(3, activation='softmax'))
# network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
network.save_weights('d:/Program_Data/model_weights_k_2.h5', overwrite=True)

for i in range(epochs):
    for k,j in enumerate(filelist):
        # if k == train_limit:
        #     break
        network.load_weights('d:/Program_Data/model_weights_k_2.h5')
        # print('*****************************')
        # print(network.get_weights())
        # print('*****************************\n\n')
        filename1 = fpath2 + j
        print('%d th epoch : ' %(i+1), filename1)
        train_data, train_labels = k0.generate_train_data_2(filename1)
        network.fit(train_data, train_labels, epochs=15, batch_size=batch_size)
        network.save_weights('d:/Program_Data/model_weights_k_2.h5', overwrite=True)
        # print('+++++++++++++++++++++++++++++++++')
        # print(network.get_weights())
        # print('+++++++++++++++++++++++++++++++++\n\n')
## test session
    # total_acc = 0
    # for j,k in enumerate(testlist):
    #     # if j == test_limit:
    #     #     break
    #     filename2 = fpath2 + k
    #     print(filename2)
    #     test_data, test_labels = k0.generate_train_data_2(filename2)
    #     test_loss, test_acc = network.evaluate(test_data, test_labels)
    #     total_acc += test_acc
    # print('test_acc: ', total_acc/test_limit)










## endl
