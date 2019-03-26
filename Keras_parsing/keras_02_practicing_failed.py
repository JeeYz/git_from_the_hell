# @Author: J.Y.
# @Date:   2019-03-21T12:09:10+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-21T14:50:40+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import os
import sys
sys.path.append(r'./module')

import keras_module_0 as k0

from keras.layers import Input, Dense
from keras.models import Model, Sequential
from keras.models import model_from_json
import numpy
import os

batch_size = 128
epochs = 10
w_vec_size = 128
p_vec_size = 73
input_size = (18*w_vec_size*2 + 18*p_vec_size*2)

fpath2 = 'd:/Program_Data/Parsing_Data/'
filelist = list()

# fix random seed for reproducibility
model = Sequential()

model.add(Dense(512, activation='relu', input_shape=(input_size, )))
model.add(Dense(3, activation='softmax'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
for i in range(epochs):
    if i != 0:
        model.load_weights('d:/Program_Data/model_weights_k_2.h5')
    # Fit the model
    filename1 = fpath2 + 'result_train_dataset_000.train'
    train_data, train_labels = k0.generate_train_data_2(filename1)
    model.fit(train_data, train_labels, epochs=1, batch_size=batch_size)
    model.save_weights('d:/Program_Data/model_weights_k_2.h5')
    print('%d epoch complete!!' %(i+1))

# evaluate loaded model on test data
filename2 = fpath2 + 'result_test_dataset_000.test'
test_data, test_labels = k0.generate_train_data_2(filename2)
test_loss, test_acc = model.evaluate(test_data, test_labels)
print('test_acc: ', test_acc)











## endl
