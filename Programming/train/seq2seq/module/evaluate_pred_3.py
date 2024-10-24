# -*- coding: utf-8 -*-

import numpy as np

none_num = 17

def evaluate_recall_(pred, y_test):
    whole_true_num = 0
    num_of_correct = 0
    for i in range(len(y_test)):
        for j in range(len(y_test[i])):
            if y_test[i][j] < none_num and y_test[i][j] != 0:
                whole_true_num += 1
                if y_test[i][j] == pred[i][j]:
                    num_of_correct += 1
    
    return num_of_correct/whole_true_num


def evaluate_precision_(pred, y_test, num_words):
    whole_pred_num = 0
    num_of_correct = 0
    for i in range(len(num_words)):
        for j in range(num_words[i]):
            if pred[i][j] < none_num and pred[i][j] != 0:
                whole_pred_num += 1
                if y_test[i][j] == pred[i][j]:
                    num_of_correct += 1
    if whole_pred_num == 0:
        return 0
    else:
        return num_of_correct/whole_pred_num


def evaluate_accuracy_(pred, y_test):
    whole_true_num = 0
    num_of_correct = 0
    for i in range(len(y_test)):
        for j in range(len(y_test[i])):
            whole_true_num += 1
            if y_test[i][j] == pred[i][j]:
                num_of_correct += 1
    
    return num_of_correct/whole_true_num


def evaluate_acc_prec_rec_f1(pred, y_test):
    num_of_words = list()
    
    for i in range(len(y_test)):
        num_of_words.append(len(y_test[i]))
    
    
    recall = evaluate_recall_(pred, y_test)
    precision = evaluate_precision_(pred, y_test, num_of_words)
    accuracy = evaluate_accuracy_(pred, y_test)
    if (recall + precision) == 0:
        f1_score = 0.
    else:
        f1_score = 2*(recall*precision)/(recall + precision)
    
    
    return accuracy, precision, recall, f1_score

def make_confusion_matrix(pred, yd, c_mat):
   
    for j in range(len(yd)):
        for i in range(len(yd[j])):
            # if int(yd[j][i]) < 23 and int(yd[j][i]) != 20:
            # if int(yd[j][i]) < 23:
            c_mat[int(yd[j][i])][int(pred[j][i])] += 1
            
    return c_mat
    
# def evaluate_acc(c_mat, soo):
#     total_num = np.sum(c_mat)    
#     c_num = 0
#     for i in range(1, none_num):
#         c_num += np.sum(c_mat[i])        
    
#     return (c_num / total_num)
   

# def evaluate_recall(c_mat, soo):
#     c_num = 0
#     total_num = 0
#     for i in range(1, none_num):
#         total_num += np.sum(c_mat[i])
        
#     for i in range(1, none_num):
#         c_num += c_mat[i][i]
    
#     return (c_num/total_num)


# def evaluate_precision(c_mat, soo):
#     c_num = 0
#     total_num = 0
#     for j in range(1, none_num):
#         for i in range(1, soo):
#             total_num += c_mat[i][j]
    
#     for i in range(1, none_num):
#         c_num += c_mat[i][i]
        
#     return (c_num/total_num)
    
    


# def evaluate_f1score(c_mat, soo):
#     recall = evaluate_recall(c_mat, soo)
#     precision = evaluate_precision(c_mat, soo)
#     print("recall : %f" %recall)
#     print("precision : %f" %precision)
#     return 2*recall*precision/(recall+precision)


# def evaluate_all(c_mat, soo):
    
#     acc = evaluate_acc(c_mat, soo)        
#     f1_score = evaluate_f1score(c_mat, soo)
            
#     return acc, f1_score