# @Author: J.Y.
# @Date:   2019-03-21T15:47:00+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-21T15:52:20+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import os
import sys
sys.path.append(r'./module')

from keras import models
from keras import layers
from keras.models import load_model
from keras.layers import Input, Dense
from keras.models import Model, Sequential

import keras_module_0 as k0

batch_size = 128
epochs = 10
w_vec_size = 128
p_vec_size = 73
input_size = (18*w_vec_size*2 + 18*p_vec_size*2)

fpath2 = 'd:/Program_Data/Parsing_Data/'
filelist = list()
for (path, dir, files) in os.walk("d:/Program_Data/Parsing_Data/"):
    for filename in files:
        if '.train' in filename:
            filelist.append(filename)
filelist = tuple(filelist)
# print(filelist)
testlist = list()
for (path, dir, files) in os.walk("d:/Program_Data/Parsing_Data/"):
    for filename in files:
        if '.test' in filename:
            testlist.append(filename)
testlist = tuple(testlist)

network = models.Sequential()

network.add(layers.Dense(512, activation='relu', input_shape=(input_size, )))
network.add(layers.Dense(3, activation='softmax'))

# network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
network.save_weights('d:/Program_Data/model_weights_k_1.h5', overwrite=True)
for j in filelist:
    for i in range(epochs):
        network.load_weights('d:/Program_Data/model_weights_k_1.h5')
        # b = network.get_weights()
        # print('*****************************')
        # print(b)
        # print('*****************************\n\n')
        filename1 = fpath2 + j
        train_data, train_labels = k0.generate_train_data_2(filename1)
        network.fit(train_data, train_labels, epochs=10, batch_size=batch_size)
        network.save_weights('d:/Program_Data/model_weights_k_1.h5', overwrite=True)
        # a = network.get_weights()
        # print('+++++++++++++++++++++++++++++++++')
        # print(a)
        # print('+++++++++++++++++++++++++++++++++\n\n')

# filename1 = fpath2 + 'result_train_dataset_000.train'
# train_data, train_labels = k0.generate_train_data_2(filename1)
# network.fit(train_data, train_labels, epochs=epochs, batch_size=batch_size)

## test session
# filename2 = fpath2 + 'result_test_dataset_000.test'
# test_data, test_labels = k0.generate_train_data_2(filename2)
# test_loss, test_acc = network.evaluate(test_data, test_labels)
# print('test_acc: ', test_acc)
total_acc = 0
for k in testlist:
    filename2 = fpath2 + k
    test_data, test_labels = k0.generate_train_data_2(filename2)
    test_loss, test_acc = network.evaluate(test_data, test_labels)
    total_acc += test_acc
print('test_acc: ', test_acc/100)














## endl
