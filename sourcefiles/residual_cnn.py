# -*- coding: utf-8 -*-

'''
residual convolution nn
'''

#%% declaration
import sys
sys.path.append("C:\\Users\\jyback_pnc\\Desktop\\code\\girl_from_ipanema")

import numpy as np
import tensorflow as tf
from tensorflow import keras
from draw_graph import result_graph as rg
from module import save_the_best as save_best
from make_train_data import load_train_data_class as load_data_cl

from variables import raw_list, mfcc_list_13, mfcc_list_26, logfb_list
from variables import normal_mfcc13_list, normal_mfcc26_list, normal_logfb_list, normal_raw_sig

train_data_path = "../"

file_list = normal_raw_sig

import basic_rnn_class as brnncl
import basic_cnn_block as bcblock
import residual_block as resnet_block
import residual_block_1D as resnet_1D

num_batch = 16
epoch_num = 150
num_label = 16

load_mode = 0


#%% loading data
load_data_class = load_data_cl(files_list=file_list, npz_path=train_data_path)
train_mfcc_feats, test_mfcc_feats, train_labels, test_labels, conv_shape \
    = load_data_class.load_train_data(1, 3, load_train_kind='raw_signal',
                                      max_number=80000)


#%% build model
input_vec = tf.keras.Input(shape=conv_shape)
# print(conv_shape)
# resnet = resnet_block.residual_net(pooling_bool=False, kernel_size=(3, 3))

resnet = resnet_1D.residual_net_1D(pooling_bool=False, kernel_size=5, strides_size=1)

answer = resnet(input_vec, num_of_classes=num_label, dense_softmax=True)

model = tf.keras.Model(inputs=input_vec, outputs=answer)

model.summary()

model.compile(optimizer=keras.optimizers.Adam(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


#%% epoch training loop
graph_cl = rg()
max_metr = save_best(file_name='highest_metrics_resnet.txt')
max_metr.load_best_metrics()
max_acc = max_metr.max_metrics
print(max_metr.max_metrics)
temp = 0.0


#%% new train // validation
# if load_mode == 1:
#     model.load_weights('save_weight/resnet_model.h5')

# history = model.fit(train_mfcc_feats, train_labels, 
#                         batch_size=num_batch, epochs=epoch_num,
#                         validation_split=0.05)

# loss, metric_res = model.evaluate(x=test_mfcc_feats, 
#         y=test_labels, verbose=1)   # "return_dict" argument doesn't work in tf 2.1 
#                                     # but, after 2.2, it workss
# model.save('save_weight/rnn_cnn_model.h5')

# graph_cl.draw_train_val_graph(history.history)


#%% old train // test per one epoch
for i,epo in enumerate(range(epoch_num)):
    print("\n\n%d th epoch\n"%(epo+1))
    
    if load_mode == 1:
        model.load_weights('save_weight/resnet_model.h5')
    
    history = model.fit(train_mfcc_feats, train_labels, 
                            batch_size=num_batch, epochs=1)
    
    loss, metric_res = model.evaluate(x=test_mfcc_feats, 
            y=test_labels, verbose=1)   # "return_dict" argument doesn't work in tf 2.1 
                                        # but, after 2.2, it workss
    model.save('save_weight/resnet_model.h5')
    if metric_res > max_acc:
        max_metr.write_best_metrics(kind_of_metric='accuracy', 
                                    metric_result=metric_res)
        max_acc = metric_res
        model.save('save_weight/resnet_model_best.h5')
        print("recent max acc value : ", max_metr.max_metrics)
    
    if metric_res > temp:
        temp = metric_res
    
    graph_cl.make_list(train_result=history, eval_loss=loss, eval_acc=metric_res)
    

graph_cl.draw_plt_graph()
print("\nhighest accuracy in this model only : ", temp, '\n\n\n')


#%% end of file



