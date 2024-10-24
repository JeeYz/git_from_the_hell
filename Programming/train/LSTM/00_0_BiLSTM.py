# -*- coding: utf-8 -*-


#%% declare train files

# =============================================================================
# LSTM files list
# =============================================================================
wfile1 = '../../traindata/LSTM/0_0_LSTM_train_w_f.txt'
wfile2 = '../../traindata/LSTM/0_0_LSTM_test_w_f.txt'

wfile3 = '../../traindata/LSTM/0_0_LSTM_train_w_m.txt'
wfile4 = '../../traindata/LSTM/0_0_LSTM_test_w_m.txt'

wfile5 = '../../traindata/LSTM/0_0_LSTM_train_w_b.txt'
wfile6 = '../../traindata/LSTM/0_0_LSTM_test_w_b.txt'

wfile7 = '../../traindata/LSTM/0_1_LSTM_train_w_f.txt'

wfile9 = '../../traindata/LSTM/0_1_LSTM_train_w_b.txt'






#%% pos
pfile1 = '../../traindata/LSTM/0_0_LSTM_train_p_f.txt'
pfile2 = '../../traindata/LSTM/0_0_LSTM_test_p_f.txt'

pfile3 = '../../traindata/LSTM/0_0_LSTM_train_p_m.txt'
pfile4 = '../../traindata/LSTM/0_0_LSTM_test_p_m.txt'

pfile5 = '../../traindata/LSTM/0_0_LSTM_train_p_b.txt'
pfile6 = '../../traindata/LSTM/0_0_LSTM_test_p_b.txt'






#%% syl
sfile1 = '../../traindata/LSTM/0_0_LSTM_train_s_f.txt'
sfile2 = '../../traindata/LSTM/0_0_LSTM_test_s_f.txt'

sfile3 = '../../traindata/LSTM/0_0_LSTM_train_s_m.txt'
sfile4 = '../../traindata/LSTM/0_0_LSTM_test_s_m.txt'

sfile5 = '../../traindata/LSTM/0_0_LSTM_train_s_b.txt'
sfile6 = '../../traindata/LSTM/0_0_LSTM_test_s_b.txt'






#%% 4000
sp4000_1 = '../../traindata/LSTM/0_0_LSTM_train_sp4_f.txt'
sp4000_2 = '../../traindata/LSTM/0_0_LSTM_test_sp4_f.txt'

sp4000_3 = '../../traindata/LSTM/0_0_LSTM_train_sp4_m.txt'
sp4000_4 = '../../traindata/LSTM/0_0_LSTM_test_sp4_m.txt'

sp4000_5 = '../../traindata/LSTM/0_0_LSTM_train_sp4_b.txt'
sp4000_6 = '../../traindata/LSTM/0_0_LSTM_test_sp4_b.txt'



sp4000_9 = '../../traindata/LSTM/0_1_LSTM_train_sp4_b.txt'




#%% 6000
sp6000_1 = '../../traindata/LSTM/0_0_LSTM_train_sp6_f.txt'
sp6000_2 = '../../traindata/LSTM/0_0_LSTM_test_sp6_f.txt'

sp6000_3 = '../../traindata/LSTM/0_0_LSTM_train_sp6_m.txt'
sp6000_4 = '../../traindata/LSTM/0_0_LSTM_test_sp6_m.txt'

sp6000_5 = '../../traindata/LSTM/0_0_LSTM_train_sp6_b.txt'
sp6000_6 = '../../traindata/LSTM/0_0_LSTM_test_sp6_b.txt'


# mod
sp6000_7 = '../../traindata/LSTM/0_1_LSTM_train_sp6_f_up.txt'
sp6000_8 = '../../traindata/LSTM/0_2_LSTM_train_sp6_f_up.txt'
sp6000_9 = '../../traindata/LSTM/0_3_LSTM_train_sp6_f_up.txt'




#%% 8000
sp8000_1 = '../../traindata/LSTM/0_0_LSTM_train_sp8_f.txt'
sp8000_2 = '../../traindata/LSTM/0_0_LSTM_test_sp8_f.txt'

sp8000_3 = '../../traindata/LSTM/0_0_LSTM_train_sp8_m.txt'
sp8000_4 = '../../traindata/LSTM/0_0_LSTM_test_sp8_m.txt'

sp8000_5 = '../../traindata/LSTM/0_0_LSTM_train_sp8_b.txt'
sp8000_6 = '../../traindata/LSTM/0_0_LSTM_test_sp8_b.txt'



sp8000_7 = '../../traindata/LSTM/0_1_LSTM_train_sp8_f.txt'



sp8000_9 = '../../traindata/LSTM/0_1_LSTM_train_sp8_b.txt'




# =============================================================================
# =============================================================================
# =============================================================================
# # # 
# =============================================================================
# =============================================================================
# =============================================================================


#%% declare base
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import sys
import numpy as np
import os
import tensorflow_addons as tfa

print('Python version : ', sys.version)
print('TensorFlow version : ', tf.__version__)
print('Keras version: ', keras.__version__)

#%% load data

from module.read_data_2 import load_LSTM_data as lld
from module.read_data_2 import make_class_weight as mcw

f1 = sp6000_7
f2 = sp6000_2

x_train, y_train, x_test, y_test = lld(f1, f2)

batch_num = 128
Epoch = 1

VEC_SIZE = 256
# WORDS_SIZE = 4001+1
WORDS_SIZE = 6001+1
# WORDS_SIZE = 8001+1
# WORDS_SIZE = 8616+1
# WORDS_SIZE = 18086+1

# size_of_output = 23+1
size_of_output = 24+1
                        
#%% input layer   
w_input = tf.keras.Input(shape=(None,), name='w_input')

embedding_layer_1 = layers.Embedding(WORDS_SIZE, VEC_SIZE,
                                    mask_zero=True,
                                    trainable=True,
                                    embeddings_initializer='random_normal')


#%% embedding
x = embedding_layer_1(w_input)

#%% LSTM layer
x = layers.Bidirectional(layers.GRU(128, return_sequences=True))(x)
x = layers.Bidirectional(layers.GRU(128, return_sequences=True))(x)
x = layers.Bidirectional(layers.GRU(64, return_sequences=True))(x)
# x = layers.Bidirectional(layers.LSTM(128, return_sequences=True))(x)



#%% output layer
# x = layers.TimeDistributed(layers.Dense(128))(x)
answer = layers.TimeDistributed(layers.Dense(size_of_output, 
                                              activation='sigmoid'))(x)


#%% model declaration
model = tf.keras.Model(inputs=w_input, outputs=answer)
model.summary()


#%% train
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
#                 metrics=['accuracy'])

model.compile('sgd', loss=tfa.losses.SigmoidFocalCrossEntropy())
# model.compile(optimizer='sgd',
#               loss='sparse_categorical_crossentropy',
#                 metrics=['accuracy'])

x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, 
                                                       padding = 'post')
y_train = tf.keras.preprocessing.sequence.pad_sequences(y_train, 
                                                       padding = 'post')


#%% class weight
w1 = 1.e-40
w2 = 1.e-8
w3 = 25.
class_weight = mcw(size_of_output, w1, w2, w3)


#%% check point setting
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

# model = create_model()
model.load_weights(checkpoint_path)

history = model.fit(x_train, y_train, class_weight=class_weight,
                    batch_size=batch_num, epochs=Epoch, callbacks=[cp_callback])

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
from module.evaluate_pred_2 import make_confusion_matrix as mcm
from module.evaluate_pred_2 import evaluate_all as eall
from module.evaluate_pred_2 import evaluate_acc_prec_rec_f1 as eval_all

x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, 
                                                       padding = 'post')

pred = model.predict(x_test)
pred = np.argmax(pred, axis=2)
print(pred)

conf_matrix = np.zeros((size_of_output, size_of_output), dtype='int')
       
conf_matrix = mcm(pred, y_test, conf_matrix)
     
acc, f1_score = eall(conf_matrix, size_of_output)

print("accuracy : %f" %acc)
print("f1 score : %f" %f1_score)

acc, prec, rec, f1 = eval_all(pred, y_test)
print('accuracy : %f' %acc)
print('precision : %f' %prec)
print('recall : %f' %rec)
print('f1 score : %f' %f1)






















