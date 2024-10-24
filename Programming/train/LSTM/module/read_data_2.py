# -*- coding: utf-8 -*-

import numpy as np

def make_class_weight(class_weights):
    result = dict()
    result[0] = 0.
    for i,w in enumerate(class_weights):
        result[i+1] = w
    
    result[2] *= 2
    # result[17] *= 1.e-2
    # result[21] *= 1.e-2
    return result

def load_LSTM_data(trainf, testf):
    x_train, y_train, x_test, y_test = list(), list(), list(), list()
    y_cl = list()
    with open(trainf, 'r', encoding='utf-8') as rf0,\
    open(testf, 'r', encoding='utf-8') as rf1:
        while True:
            l0 = rf0.readline()
            l1 = rf0.readline()
            l2 = rf0.readline()
            if not l0:break
            l0 = l0.split()
            l1 = l1.split()
            
            line0, line1 = list(), list()
            
            for i in l0:
                line0.append(float(i))
            for i in l1:
                line1.append(float(i))
            for i in l1:
                y_cl.append(int(i))
            
            x_train.append(line0)
            y_train.append(line1)
            
        
        while True:
            l0 = rf1.readline()
            l1 = rf1.readline()
            l2 = rf1.readline()
            if not l0:break
            l0 = l0.split()
            l1 = l1.split()
            
            line0, line1 = list(), list()
            
            for i in l0:
                line0.append(float(i))
            for i in l1:
                line1.append(float(i))
            
            x_test.append(line0)
            y_test.append(line1)
        
    x_train = np.asarray(x_train)
    y_train = np.asarray(y_train)
    x_test = np.asarray(x_test)
    y_test = np.asarray(y_test)
        
    return x_train, y_train, x_test, y_test, y_cl