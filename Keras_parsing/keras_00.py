# @Author: J.Y.
# @Date:   2019-02-26T04:47:06+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-19T12:29:54+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

from keras import models
from keras import layers

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28, )))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

network.summary()
# print(train_images)

print(type(train_images))

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
