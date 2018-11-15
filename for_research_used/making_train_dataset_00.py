# @Author: JayY
# @Date:   2018-10-02T15:34:05+09:00
# @Filename: new_34.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-07T15:51:26+09:00
# @Copyright: JayY

# @new_34.py

# making for traing data
# structure : center_word \t target_word \t path
# =============================================


import copy
import collections
import numpy as np
import random
import sys
sys.setrecursionlimit(50000)

filename0 = './data/korean_wiki/korean_wiki_result_words_02_huff_words.txt'
filename1 = './data/korean_wiki/korean_wiki_result_words_03_huff_nodes.txt'
filename2 = './data/korean_wiki/korean_wiki_temp_data_sents_changed.txt'

filename3 = './data/korean_wiki/korean_wiki_result_data_for_training_full.txt'

f_read1 = open(filename0, 'r', encoding='utf-8') # words data
f_read2 = open(filename1, 'r', encoding='utf-8') # nodes data
# fp = open('result_sent_02.txt', 'r', encoding='utf-8')
fp = open(filename2, 'r', encoding='utf-8')
fpw = open(filename3, 'w', encoding='utf-8')

window_size = 5
skip_num = window_size*2
num_skip = skip_num + 1

def make_dict_data():
    dict_word = dict()
    dict_node = dict()
    dict_node_path = dict()
    while True:
        line = f_read1.readline().split()
        if not line : break
        dict_word[line[0]] = list()
        dict_word[line[0]].append(line[1])
        dict_word[line[0]].append(line[4:])
    while True:
        line = f_read2.readline().split()
        if not line: break
        dict_node[line[0]] = list()
        dict_node[line[0]].append(line[1])
        dict_node[line[0]].append(line[4:])
        a = str(line[4:])
        #print(a)
        dict_node_path[a] = line[1]
    return dict_word, dict_node, dict_node_path

dict_word, dict_node, dict_node_path = make_dict_data()

def make_train_file(dict_node, dict_word, dict_node_path):
    while True:
        line = fp.readline()
        if not line: break
        line = line.split()
        num = len(line)

        for i in range(1, (num-1)):
            # print('hello, world', i, line[i])
            if i <= window_size:
                s_i = 0
            else:
                s_i = i - window_size

            if window_size >= (num - 1 - i):
                e_i = num
            else:
                e_i = i + window_size + 1

            for j in range(s_i, e_i):
                if i == j: continue
                cword = str(dict_word.get(line[i])[0])
                # print(i, line[i], '\t', j, line[j])
                all_path = copy.deepcopy(dict_word.get(line[j])[1])
                curr_path = list()
                idx = 0 # this is root node
                for k in all_path:
                    fpw.write(cword + '\t'*2 + str(idx) + '\t'*2 + str(k) + '\n')
                    curr_path.append(k)
                    idx = dict_node_path.get(str(curr_path))

make_train_file(dict_node, dict_word, dict_node_path)
