# -*- coding: utf-8 -*-

import numpy as np

def load_FNN_data(trainf, testf):
    x_train, y_train, x_test, y_test = list(), list(), list(), list()
    with open(trainf, 'r', encoding='utf-8') as rf0,\
    open(testf, 'r', encoding='utf-8') as rf1:
        while True:
            l0 = rf0.readline()            
            if not l0:break
            l0 = l0.split()
            
            line0 = list()
            
            for i in l0[:-1]:
                line0.append(int(i))
            
            x_train.append(line0)
            # y_train.append([int(l0[-1])])
            y_train.append(int(l0[-1]))
        
        while True:
            l0 = rf1.readline()
            if not l0:break
            l0 = l0.split()
            
            line0 = list()
            
            for i in l0[:-1]:
                line0.append(int(i))
            
            x_test.append(line0)
            # y_test.append([int(l0[-1])])
            y_test.append(int(l0[-1]))
        
    x_train = np.asarray(x_train)
    y_train = np.asarray(y_train)
    x_test = np.asarray(x_test)
    y_test = np.asarray(y_test)
        
    return x_train, y_train, x_test, y_test

