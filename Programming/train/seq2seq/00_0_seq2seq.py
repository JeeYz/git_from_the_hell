# -*- coding: utf-8 -*-


#%% declare train files

# =============================================================================
# LSTM files list
# =============================================================================

#%% pos
pfile1 = '../../traindata/LSTM/0_0_LSTM_train_p_f.txt'
pfile2 = '../../traindata/LSTM/0_0_LSTM_test_p_f.txt'

pfile3 = '../../traindata/LSTM/0_0_LSTM_train_p_b.txt'
pfile4 = '../../traindata/LSTM/0_0_LSTM_test_p_b.txt'

#mod
pfile5 = '../../traindata/LSTM/1_0_LSTM_train_p_f_sample.txt'
pfile6 = '../../traindata/LSTM/1_0_LSTM_train_p_b_sample.txt'

#%% 4000
sp4000_1 = '../../traindata/LSTM/0_0_LSTM_train_sp4_f.txt'
sp4000_2 = '../../traindata/LSTM/0_0_LSTM_test_sp4_f.txt'

sp4000_3 = '../../traindata/LSTM/0_0_LSTM_train_sp4_b.txt'
sp4000_4 = '../../traindata/LSTM/0_0_LSTM_test_sp4_b.txt'

# mod
sp4000_5 = '../../traindata/LSTM/1_0_LSTM_train_sp4_f_sample.txt'
sp4000_6 = '../../traindata/LSTM/1_0_LSTM_train_sp4_b_sample.txt'


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

from module.read_data_3 import load_LSTM_data as lld
from module.read_data_3 import make_class_weight as mcw

train_file = '../../traindata/LSTM/srl_train_pos.txt'
test_file = '../../traindata/LSTM/srl_test_pos.txt'

f1 = train_file
f2 = test_file

x_train, y_train, x_test, y_test, y_cl = lld(f1, f2)

batch_num = 32
Epoch = 20
load_para = 1
one_load = 0
focal_usage = 0

VEC_SIZE = 256
# WORDS_SIZE = 5000+1
WORDS_SIZE = 10000
# WORDS_SIZE = 20000

# size_of_output = 20+1
size_of_output = 42+1
                        

#%% input layer  && embedding 
w_input = tf.keras.Input(shape=(None,), name='w_input')

embedding_layer_1 = layers.Embedding(WORDS_SIZE, VEC_SIZE,
                                    mask_zero=True)
# embedding_layer_2 = layers.Embedding(WORDS_SIZE, VEC_SIZE,
#                                     mask_zero=True)

x = embedding_layer_1(w_input)


#%% encoder

num_hidden = 512
num_att_hidden = 512

whole_seq_output, final_memory_state = \
    layers.GRU(num_hidden, return_sequences=True, return_state=True)(x)

#%% attention

# y = tf.concat([final_carry_state, final_memory_state], -1)
y = tf.expand_dims(final_memory_state, 1)
y = layers.Dense(num_att_hidden)(y)

x = layers.Dense(num_att_hidden)(whole_seq_output)
out = tf.nn.tanh(x+y)

attention_weight = tf.nn.softmax(out, axis=1)

context_vector = x*attention_weight
# context_vector = tf.reduce_sum(context_vector, axis=1)

#%% decoder

x = embedding_layer_1(w_input)

new_input = tf.concat([context_vector, x], axis=-1)

x = layers.Bidirectional(layers.GRU(num_hidden, return_sequences=True))(new_input)
x = layers.Bidirectional(layers.GRU(num_hidden, return_sequences=True))(x)
# x = layers.GRU(num_hidden, return_sequences=True)(new_input)



#%% output layer
x = layers.TimeDistributed(layers.Dense(512))(x)
x = layers.Dropout(0.2)(x)
answer = layers.TimeDistributed(layers.Dense(size_of_output, 
                                              activation='softmax'))(x)
# answer = layers.Dense(size_of_output, activation='softmax')(x)


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
    model.compile(optimizer='adam',
                    # optimizer=tf.keras.optimizers.Adam(),
                    loss='sparse_categorical_crossentropy',
                   metrics=['accuracy'])


#%% for
maximum = [0., 0., 0., 0.]
for epo in range(Epoch):
    print('%d th epoch ~!!'%epo)

#%% check point setting
    checkpoint_path = "training_1/cp.ckpt"
    checkpoint_dir = os.path.dirname(checkpoint_path)
    
    cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                     save_weights_only=True,
                                                     verbose=1)
    
    if one_load == 0:
        if load_para == 1:
            if epo != 0:
                model.load_weights(checkpoint_path)
    else:
        model.load_weights(checkpoint_path)
   
       
    #%% class weight
    class_weights = class_weight.compute_class_weight('balanced',
                                                     np.unique(y_cl), y_cl)
    
    class_weights = mcw(class_weights)
    
    
        
    x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, 
                                                           padding = 'post')
    y_train = tf.keras.preprocessing.sequence.pad_sequences(y_train, 
                                                            padding = 'post')
    
    
    #%% fit
    if focal_usage == 1:
        history = model.fit(x_train, y_train, 
                        batch_size=batch_num, epochs=Epoch, callbacks=[cp_callback])
    else:
        history = model.fit(x_train, y_train, 
                            # class_weight=class_weights,
                            epochs=1, callbacks=[cp_callback])
    
    
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
    from module.evaluate_pred_3 import make_confusion_matrix as mcm
    from module.evaluate_pred_3 import evaluate_acc_prec_rec_f1 as eval_all
    
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

    
    if maximum[3] < f1:
        maximum = [acc, rec, prec, f1]
      

    print('\n')
    print('* * * Maximum f1 score * * *')
    print('accuracy : %f' %maximum[0])
    print('recall : %f' %maximum[1])
    print('precision : %f' %maximum[2])
    print('f1 score : %f' %maximum[3])
    print('\n')

























