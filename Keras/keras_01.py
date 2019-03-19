# @Author: J.Y.
# @Date:   2019-03-13T16:34:16+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-19T11:34:06+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import sys
sys.path.append(r'./module')

from keras import models
from keras import layers

import keras_module_0 as k0

batch_size = 128
epochs = 10
w_vec_size = 128
p_vec_size = 73
input_size = (18*w_vec_size + 18*p_vec_size)

filepath = 'd:/Program_Data/'
filelist = list()

## full dataset.
# for i in range(1):
#     filelist.append(filepath + 'result_train_dataset_%02d.train' %i)
# filetuple = tuple(filelist)

## one dataset for practicing
filename1 = filepath + 'result_train_dataset_000.train'
filename2 = filepath + 'raw_test_dataset_04.test'

# train_data, train_labels = k0.generate_train_data(filename, batch_size)
train_data, train_labels = k0.generate_train_data(filename1, batch_size)
test_data, test_labels = k0.generate_train_data(filename2, batch_size)

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(input_size, )))
network.add(layers.Dense(3, activation='softmax'))

network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

network.summary()
# print(train_images)

# train_data, train_labels = k0.generate_train_data(filename1, batch_size)
# test_data, test_labels = k0.generate_train_data(filename2, batch_size)

network.fit(train_data, train_labels, epochs=epochs, batch_size=batch_size)
# print(train_images)

## test session
test_loss, test_acc = network.evaluate(test_data, test_labels)
print('test_acc: ', test_acc)





## endl
