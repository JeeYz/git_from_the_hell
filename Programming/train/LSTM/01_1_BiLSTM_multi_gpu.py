# -*- coding: utf-8 -*-


#%% declare train files

# =============================================================================
# LSTM files list
# =============================================================================
wfile1 = '../../traindata/LSTM/0_0_LSTM_train_w_f.txt'
wfile2 = '../../traindata/LSTM/0_0_LSTM_test_w_f.txt'

wfile3 = '../../traindata/LSTM/0_0_LSTM_train_w_b.txt'
wfile4 = '../../traindata/LSTM/0_0_LSTM_test_w_b.txt'

#mod
wfile5 = '../../traindata/LSTM/1_0_LSTM_train_w_f_sample.txt'
wfile6 = '../../traindata/LSTM/1_0_LSTM_train_w_b_sample.txt'


#%% pos
pfile1 = '../../traindata/LSTM/0_0_LSTM_train_p_f.txt'
pfile2 = '../../traindata/LSTM/0_0_LSTM_test_p_f.txt'

pfile3 = '../../traindata/LSTM/0_0_LSTM_train_p_b.txt'
pfile4 = '../../traindata/LSTM/0_0_LSTM_test_p_b.txt'

#mod
pfile5 = '../../traindata/LSTM/1_0_LSTM_train_p_f_sample.txt'
pfile6 = '../../traindata/LSTM/1_0_LSTM_train_p_b_sample.txt'

#%% syl
sfile1 = '../../traindata/LSTM/0_0_LSTM_train_s_f.txt'
sfile2 = '../../traindata/LSTM/0_0_LSTM_test_s_f.txt'

sfile3 = '../../traindata/LSTM/0_0_LSTM_train_s_b.txt'
sfile4 = '../../traindata/LSTM/0_0_LSTM_test_s_b.txt'

#mod
sfile5 = '../../traindata/LSTM/1_0_LSTM_train_s_f_sample.txt'
sfile6 = '../../traindata/LSTM/1_0_LSTM_train_s_b_sample.txt'

#%% 4000
sp4000_1 = '../../traindata/LSTM/0_0_LSTM_train_sp4_f.txt'
sp4000_2 = '../../traindata/LSTM/0_0_LSTM_test_sp4_f.txt'

sp4000_3 = '../../traindata/LSTM/0_0_LSTM_train_sp4_b.txt'
sp4000_4 = '../../traindata/LSTM/0_0_LSTM_test_sp4_b.txt'

# mod
sp4000_5 = '../../traindata/LSTM/1_0_LSTM_train_sp4_f_sample.txt'
sp4000_6 = '../../traindata/LSTM/1_0_LSTM_train_sp4_b_sample.txt'



#%% 6000
sp6000_1 = '../../traindata/LSTM/0_0_LSTM_train_sp6_f.txt'
sp6000_2 = '../../traindata/LSTM/0_0_LSTM_test_sp6_f.txt'

sp6000_3 = '../../traindata/LSTM/0_0_LSTM_train_sp6_b.txt'
sp6000_4 = '../../traindata/LSTM/0_0_LSTM_test_sp6_b.txt'

# mod
sp6000_5 = '../../traindata/LSTM/1_0_LSTM_train_sp6_f_sample.txt'
sp6000_6 = '../../traindata/LSTM/1_0_LSTM_train_sp6_b_sample.txt'



#%% 8000
sp8000_1 = '../../traindata/LSTM/0_0_LSTM_train_sp8_f.txt'
sp8000_2 = '../../traindata/LSTM/0_0_LSTM_test_sp8_f.txt'

sp8000_3 = '../../traindata/LSTM/0_0_LSTM_train_sp8_b.txt'
sp8000_4 = '../../traindata/LSTM/0_0_LSTM_test_sp8_b.txt'

#mod
sp8000_5 = '../../traindata/LSTM/1_0_LSTM_train_sp8_f_sample.txt'
sp8000_6 = '../../traindata/LSTM/1_0_LSTM_train_sp8_b_sample.txt'


#%% declare base
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import sys
import numpy as np
import os

from sklearn.utils import class_weight
# import losses


print('Python version : ', sys.version)
print('TensorFlow version : ', tf.__version__)
print('Keras version: ', keras.__version__)



#%% load data

from module.read_data_2 import load_LSTM_data as lld
from module.read_data_2 import make_class_weight as mcw

f1 = sp4000_5
f2 = sp4000_2

x_train, y_train, x_test, y_test, y_cl = lld(f1, f2)

batch_num = 1024*2
Epoch = 50
load_para = 0
focal_usage = 0

VEC_SIZE = 256
WORDS_SIZE = 5000+1
# WORDS_SIZE = 10000
# WORDS_SIZE = 20000

# size_of_output = 20+1
size_of_output = 21+1
                        
#%% multi GPU
mirrored_strategy = tf.distribute.MirroredStrategy(
    cross_device_ops=tf.distribute.HierarchicalCopyAllReduce())
with mirrored_strategy.scope():

#%% input layer   
    w_input = tf.keras.Input(shape=(None,), name='w_input')
    
    embedding_layer_1 = layers.Embedding(WORDS_SIZE, VEC_SIZE,
                                        mask_zero=True)
                                        # embeddings_initializer='random_normal')
    
    
    #%% embedding
    x = embedding_layer_1(w_input)
    
    #%% LSTM layer
    # x = layers.Bidirectional(layers.LSTM(512, return_sequences=True,
    #                                       dropout=0.2, recurrent_dropout=0.2))(x)
    # x = layers.Bidirectional(layers.LSTM(512, return_sequences=True,
    #                                       dropout=0.2, recurrent_dropout=0.2))(x)
    x = layers.Bidirectional(layers.LSTM(512, return_sequences=True))(x)
    x = layers.Bidirectional(layers.LSTM(512, return_sequences=True))(x)
    
    
    #%% output layer
    x = layers.TimeDistributed(layers.Dense(512, activation='sigmoid'))(x)
    x = layers.Dropout(0.2)(x)
    answer = layers.TimeDistributed(layers.Dense(size_of_output, 
                                                  activation='sigmoid'))(x)
    
    
    #%% model declaration
    model = tf.keras.Model(inputs=w_input, outputs=answer)
    model.summary()
    
    
    #%% train
    if focal_usage == 1:
        import tensorflow_addons as tfa
        y_train = tf.one_hot(y_train, size_of_output,
                             on_value=1.0, off_value=0.0,
                             axis=-1)                                                           
        model.compile(optimizer='adam',
                      loss=tfa.losses.SigmoidFocalCrossEntropy(),
                       metrics=['accuracy'])
        
    else:
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.000001),
                        loss='sparse_categorical_crossentropy',
                       metrics=['accuracy'])


    
    #%% check point setting
    checkpoint_path = "training_1/cp.ckpt"
    checkpoint_dir = os.path.dirname(checkpoint_path)
    
    cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                     save_weights_only=True,
                                                     verbose=1)
    
    # model = create_model()
    if load_para == 1:
        model.load_weights(checkpoint_path)
    # dataset = tf.data.Dataset.from_tensors(x_train)


#%% class weight
class_weights = class_weight.compute_class_weight('balanced',
                                                 np.unique(y_cl), y_cl)

class_weights = mcw(class_weights)


    
x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, 
                                                       padding = 'post')
y_train = tf.keras.preprocessing.sequence.pad_sequences(y_train, 
                                                        padding = 'post')

dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(batch_num)


#%% fit
if focal_usage == 1:
    history = model.fit(x_train, y_train, 
                    batch_size=batch_num, epochs=Epoch, callbacks=[cp_callback])
else:
    history = model.fit(dataset,
                       # x_train, y_train, 
                        # class_weight=class_weights,
                        epochs=Epoch, callbacks=[cp_callback])


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
from module.evaluate_pred_2 import evaluate_acc_prec_rec_f1 as eval_all

x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, 
                                                       padding = 'post')

pred = model.predict(x_test)
pred = np.argmax(pred, axis=2)
print(pred)

conf_matrix = np.zeros((size_of_output, size_of_output), dtype='int')
       
conf_matrix = mcm(pred, y_test, conf_matrix)

acc, prec, rec, f1 = eval_all(pred, y_test)
print('accuracy : %f' %acc)
print('recall : %f' %rec)
print('precision : %f' %prec)
print('f1 score : %f' %f1)



























