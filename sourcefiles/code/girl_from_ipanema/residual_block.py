# -*- coding: utf-8 -*-

#%% explained
'''
class : residual cnn block
class : convolution nn with using resnet
'''


#%% declaration
from tensorflow.keras import layers
import tensorflow as tf


#%% class -> residual cnn block
class residual_cnn_block(layers.Layer):
    
    def __init__(self, **kwarg):
        super(residual_cnn_block, self).__init__()
        
        if "input_shape" in kwarg.keys():
            self.input_shape_conv = kwarg["input_shape"]
        else:
            self.input_shape_conv = None
            
        if "channel_size" in kwarg.keys():
            self.chan_size = kwarg['channel_size']
        if "kernel_size" in kwarg.keys():
            self.ker_size = kwarg['kernel_size']
        
        if "dropout_value" in kwarg.keys():
            dropout_val = kwarg["dropout_value"]
            
            
        if self.input_shape_conv:
            self.conv2d_layer_1 = layers.Conv2D(self.chan_size[0], self.ker_size, 
                                                padding='same', 
                            activation='relu', input_shape=self.input_shape_conv)
            self.conv2d_layer_2 = layers.Conv2D(self.chan_size[1], self.ker_size, 
                                                padding='same', 
                            activation='relu', input_shape=self.input_shape_conv)
        else:
            self.conv2d_layer_1 = layers.Conv2D(self.chan_size[0], self.ker_size, 
                                                padding='same', activation='relu')
            self.conv2d_layer_2 = layers.Conv2D(self.chan_size[1], self.ker_size, 
                                                padding='same', activation='relu')
            
        
    def __call__(self, broad_inputs, inputs, **kwarg):
        
        x = layers.BatchNormalization()(inputs)
        x = self.conv2d_layer_1(x)
        x = layers.BatchNormalization()(x)
        x = self.conv2d_layer_2(x)
        x = layers.Conv2D(self.chan_size[1], (1, 1), padding='same', activation='relu')(x)
        x = tf.math.add(broad_inputs, x)
                
        return x
        

#%% class -> residual net
class residual_net(layers.Layer):
    
    def __init__(self, **kwarg):
        super(residual_net, self).__init__()
        
        if "channels_size" in kwarg.keys():
            self.chan_size = kwarg["channels_size"] # init size
        if "dropout_value" in kwarg.keys():
            self.dropout_val = kwarg["dropout_value"] # init value
        if "num_of_blocks" in kwarg.keys():
            self.num_of_blocks = kwarg["num_of_blocks"]
        if "activation" in kwarg.keys():
            self.activation = kwarg["activation"]
            
        if "input_shape" in kwarg.keys():
            self.input_shape_conv = kwarg["input_shape"]
        else:
            self.input_shape_conv = False
        if "pooling_bool" in kwarg.keys():
            self.pooling_bool = kwarg["pooling_bool"]
        else:
            self.pooling_bool = False
        if "kernel_size" in kwarg.keys():
            self.ker_size = kwarg["kernel_size"]
        if "output_type" in kwarg.keys():
            # 1: 'cnn' / 2: 'rnn' / 3: 'dense' / 4: 'false'
            self.output_type = kwarg['output_type'] 

        
        # if self.input_shape_conv:
        #     self.residual_cnn_layer_1 = residual_cnn_block(channel_size=self.chan_size, 
        #                                             kernel_size=self.ker_size,
        #                                             input_shape=self.input_shape_conv)
        # else:
        self.residual_cnn_layer_1 = residual_cnn_block(channel_size=self.chan_size, 
                                                kernel_size=self.ker_size)
        self.residual_cnn_layer_2 = residual_cnn_block(channel_size=self.chan_size, 
                                                kernel_size=self.ker_size)
        self.residual_cnn_layer_3 = residual_cnn_block(channel_size=self.chan_size, 
                                                kernel_size=self.ker_size)
        self.residual_cnn_layer_4 = residual_cnn_block(channel_size=self.chan_size, 
                                                kernel_size=self.ker_size)
        self.residual_cnn_layer_5 = residual_cnn_block(channel_size=self.chan_size, 
                                                kernel_size=self.ker_size)
        self.residual_cnn_layer_6 = residual_cnn_block(channel_size=self.chan_size, 
                                                kernel_size=self.ker_size)
        self.residual_cnn_layer_7 = residual_cnn_block(channel_size=self.chan_size, 
                                                kernel_size=self.ker_size)
        self.residual_cnn_layer_8 = residual_cnn_block(channel_size=self.chan_size, 
                                                kernel_size=self.ker_size)
        self.residual_cnn_layer_9 = residual_cnn_block(channel_size=self.chan_size, 
                                                kernel_size=self.ker_size)
            
        self.pooling_layer = layers.MaxPool2D(pool_size=(4, 1), padding='same')
        
        
    def __call__(self, inputs, **kwarg):
        
        if 'num_of_classes' in kwarg.keys():
            num_class = kwarg['num_of_classes']        
        if 'dense_softmax' in kwarg.keys():
            softmax_bool = kwarg['dense_softmax']
        else:
            softmax_bool = False
        
        init_inputs = inputs
                
        x = self.residual_cnn_layer_1(init_inputs, inputs)
        if self.pooling_bool:
            x = self.pooling_layer(x)
        x = self.residual_cnn_layer_2(init_inputs, x)
        if self.pooling_bool:
            x = self.pooling_layer(x)
        x = self.residual_cnn_layer_3(init_inputs, x)
        if self.pooling_bool:
            x = self.pooling_layer(x)
        x = self.residual_cnn_layer_4(init_inputs, x)
        x = self.residual_cnn_layer_5(init_inputs, x)
        x = self.residual_cnn_layer_6(init_inputs, x)
        x = self.residual_cnn_layer_7(init_inputs, x)
        x = self.residual_cnn_layer_8(init_inputs, x)
        x = self.residual_cnn_layer_9(init_inputs, x)
        
        
        if softmax_bool:
            x = layers.GlobalAveragePooling2D()(x)
            x = layers.Flatten()(x)
            # x = layers.Dropout(0.2)(x)
            x = layers.Dense(256, activation='relu')(x)
            # x = layers.Dropout(0.3)(x)
            output_val = layers.Dense(num_class, activation='softmax')(x)
        else:
            output_val = x
        
        return output_val


#%% __main__
if __name__ == "__main__":
    print("hello, world~!")

