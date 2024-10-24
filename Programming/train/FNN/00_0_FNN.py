# -*- coding: utf-8 -*-



#%% declare train files

wfile0 = '../../traindata/FNN/0_0_FNN_train_w.txt'
wfile1 = '../../traindata/FNN/0_0_FNN_test_w.txt'

wfile2 = '../../traindata/FNN/0_0_FNN_train_p.txt'
wfile3 = '../../traindata/FNN/0_0_FNN_test_p.txt'

wfile4 = '../../traindata/FNN/0_0_FNN_train_s.txt'
wfile5 = '../../traindata/FNN/0_0_FNN_test_s.txt'

wfile6 = '../../traindata/FNN/0_0_FNN_train_4.txt'
wfile7 = '../../traindata/FNN/0_0_FNN_test_4.txt'

wfile8 = '../../traindata/FNN/0_0_FNN_train_6.txt'
wfile9 = '../../traindata/FNN/0_0_FNN_test_6.txt'

wfile10 = '../../traindata/FNN/0_0_FNN_train_8.txt'
wfile11 = '../../traindata/FNN/0_0_FNN_test_8.txt'




#%% declare base
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import sys
import numpy as np

print('Python version : ', sys.version)
print('TensorFlow version : ', tf.__version__)
print('Keras version: ', keras.__version__)

#%% load data

from module.read_data_1 import load_FNN_data as lfd

f1 = wfile0
f2 = wfile1

x_train, y_train, x_test, y_test = lfd(f1, f2)

batch_num = 256


VEC_SIZE = 128
# WORDS_SIZE = 4001+1
# WORDS_SIZE = 6001+1
# WORDS_SIZE = 8001+1
# WORDS_SIZE = 8616+1
WORDS_SIZE = 18086+1

size_of_output = 23+1
# size_of_output = 24+1
max_len = 80
                        
#%% input layer   
w_input = tf.keras.Input(shape=(max_len,), name='w_input')

embedding_layer_1 = layers.Embedding(WORDS_SIZE, VEC_SIZE,
                                    mask_zero=True,
                                    trainable=True,
                                    embeddings_initializer='random_normal')


#%% embedding
x = embedding_layer_1(w_input)
x = layers.Flatten()(x)

#%% LSTM layer
x = layers.Dense(512, activation='relu')(x)


#%% output layer
# x = layers.TimeDistributed(layers.Dense(128))(x)
answer = layers.Dense(size_of_output, activation='softmax')(x)



#%% model declaration
model = tf.keras.Model(inputs=w_input, outputs=answer)
model.summary()


#%% train
model.compile(
    optimizer='adam',
              # optimizer=tf.keras.optimizers.Adam(lr=0.0001),
              loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
               # metrics=[tf.keras.metrics.Precision(thresholds=0.5)])

x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, 
                                                        maxlen = max_len,
                                                       padding = 'post')


#%% tensorboard

history = model.fit(x_train, y_train,
                    batch_size=batch_num, epochs=10)

#%% pyplot 


import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()
acc_ax = loss_ax.twinx()

loss_ax.plot(history.history['loss'], 'y', label='train loss')
loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
loss_ax.legend(loc='upper left')

acc_ax.plot(history.history['accuracy'], 'b', label='train accuracy')
acc_ax.set_ylabel('accuracy')
acc_ax.legend(loc='upper left')

plt.show()


#%% evaluation
from module.evaluate_pred_1 import make_confusion_matrix as mcm
from module.evaluate_pred_1 import evaluate_all as eall

x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, 
                                                       maxlen = max_len,
                                                       padding = 'post')

pred = model.predict(x_test)
print(pred)
pred = np.argmax(pred, axis=1)

conf_matrix = np.zeros((size_of_output, size_of_output), dtype='int')
       
conf_matrix = mcm(pred, y_test, conf_matrix)
     
acc, f1_score = eall(conf_matrix, size_of_output)

print("accuracy : %f" %acc)
print("f1 score : %f" %f1_score)






















