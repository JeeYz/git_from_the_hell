# @Author: J.Y.
# @Date:   2019-03-13T16:34:16+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-18T10:03:33+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import sys
sys.path.append(r'/module')

from keras import models
from keras import layers

import keras_module_0 as mod0

batch_size = 128
w_vec_size = 128
p_vec_size = 73
input_size = (18*w_vec_size + 18*p_vec_size)

filepath = 'd:/Program_Data/'
filelist = list()

for i in range(1):
    filelist.append(filepath + 'result_train_dataset_%02d.train' %i)
filetuple = tuple(filelist)

for i in filetuple:
    mod1.generate_train_data(i, batch_size)

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(input_size, )))
network.add(layers.Dense(3, activation='softmax'))

network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

network.summary()
# print(train_images)

train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32')/255

test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32')/255

from keras.utils import to_categorical

## making one hot representation
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

## execution of train data
network.fit(train_images, train_labels, epochs=10, batch_size=128)
# print(train_images)
## test session
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc: ', test_acc)









## endl
