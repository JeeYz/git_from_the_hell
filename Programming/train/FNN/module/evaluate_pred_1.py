# -*- coding: utf-8 -*-

import numpy as np


def make_confusion_matrix(pred, yd, c_mat):
   
    for j in range(len(yd)):
        if int(yd[j]) < 22:
            c_mat[int(yd[j])][int(pred[j])] += 1
                
    return c_mat
    
def evaluate_acc(c_mat, soo):
    
    sum_TP = 0
    sum_all = np.sum(c_mat)
    
    for i in range(soo):
        sum_TP += c_mat[i][i]
    
    return (sum_TP / sum_all)
   

def evaluate_recall(c_mat, soo):
    sum_rec = 0
    
    for i in range(soo):
        if np.sum(c_mat[i]) == 0:
            continue
        sum_rec += c_mat[i][i]/np.sum(c_mat[i])
        
    row_num = soo - 5
    
    return sum_rec/row_num


def evaluate_precision(c_mat, soo):
    sum_prec = 0
    
    for j in range(soo):
        sum_t = 0
        for i in range(soo):
            sum_t += c_mat[i][j]
        
        if sum_t == 0:
            continue
        
        sum_prec += (c_mat[j][j]/sum_t)
        # print(sum_prec)
        
    return sum_prec/soo


def evaluate_f1score(c_mat, soo):
    recall = evaluate_recall(c_mat, soo)
    precision = evaluate_precision(c_mat, soo)
    print("recall : %f" %recall)
    print("precision : %f" %precision)
    return 2*recall*precision/(recall+precision)


def evaluate_all(c_mat, soo):
    
    acc = evaluate_acc(c_mat, soo)        
    f1_score = evaluate_f1score(c_mat, soo)
            
    return acc, f1_score