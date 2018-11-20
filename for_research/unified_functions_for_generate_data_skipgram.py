# @Author: JayY
# @Date:   2018-11-07T16:02:04+09:00
# @Filename: unified_functions_for_generate_data_00.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-08T11:05:27+09:00
# @Copyright: JayY


#
# I've combined several functions when I wanna make traindata.
# This file is a unified version.
# ==============================================================



import time
import copy
import os
import collections
import numpy as np
import random
import sys
sys.setrecursionlimit(50000)

pausing_time = 100
num_of_train_data = 51200000
reducing_barometer = 8 # reducing words

# for language model
window_size = 5
skip_num = window_size*2
num_skip = skip_num + 1

def make_dict_data(filename_r1, filename_r2):
    f_read1 = open(filename_r1, 'r', encoding='utf-8') # words data
    f_read2 = open(filename_r2, 'r', encoding='utf-8') # nodes data
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

# ==============< Excution >==============================
# dict_word, dict_node, dict_node_path = make_dict_data()
# ========================================================

def make_train_file(dict_node, dict_word, dict_node_path, filename_r, filename_w):
    fp = open(filename_r, 'r', encoding='utf-8')
    fpw = open(filename_w, 'w', encoding='utf-8')
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

# ==============< Excution >==============================
# make_train_file(dict_node, dict_word, dict_node_path)
#
# ========================================================


def reduce_words_in_dictionary(filename_r_before, filename_w_after):
    f_res = open(filename_w_after, 'w', encoding='utf-8')
    ENG_num = 0 # type -> ENGL
    NUM_num = 0 # type -> NUMB
    KAN_num = 0 # type -> KANJ
    RARE_num = 0 # type -> RARE

    rare_dict = dict()
    with open(filename_r_before, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline().split()
            if not line: break
            if line[1] == 'SH' or line[1] == 'SN' or line[1] == 'SL':
                if line[1] == 'SL':
                    ENG_num += 1
                elif line[1] == 'SN':
                    NUM_num += 1
                elif line[1] == 'SH':
                    KAN_num += 1
            elif int(line[2]) < reducing_barometer:
                if line[1] not in rare_dict:
                    rare_dict[line[1]] = 1
                else:
                    rare_dict[line[1]] += 1
            else:
                f_res.write(str(line[0]) + '\t' + str(line[1]) + '\t' + str(line[2]) + '\n')

    f_res.write('!#$_KANJI_' + '\t' + 'KANJ' + '\t' + str(KAN_num) + '\n')
    f_res.write('!#$_NUMBER' + '\t' + 'NUMB' + '\t' + str(NUM_num) + '\n')
    f_res.write('!#$_ENGLISH' + '\t' + 'ENGL' + '\t' + str(ENG_num) + '\n')
    for i in rare_dict:
        f_res.write('!#$_RARE_'+ str(i) + '\t' + str(i) + '\t' + str(rare_dict[i]) + '\n')
    f_res.close()

# ==============< Excution >==============================
#
# ========================================================

def divide_a_full_file(filename_r, filename_w):
    with open(filename_r, 'r', encoding='utf-8') as f1:
        file_num = 0
        func_button = 1
        while func_button:
            file_name = f_name + str('%03d' %file_num) + f_tail
            with open(filename_w, 'w', encoding='utf-8') as f2:
                print('hello, world', file_num)
                for i in range(num_of_train_data):
                    if i%10000000 == 0:
                        print('hello, world')
                    line  = f1.readline().split()
                    if not line:
                        func_button = 0
                        break
                    if len(line) <= 2: continue
                    f2.write(str(line[0]) + '\t' + line[1] + '\t' + line[2] + '\n')
            file_num += 1

# ==============< Excution >==============================
#
# ========================================================

def reducing_number_of_words(filename_before, filename_after, filename_r_pads, filename_w_changed):
    word_dict_before = dict()
    word_dict_after = dict()

    with open(filename_before, 'r', encoding='utf-8') as f1, open(filename_after, 'r', encoding='utf-8') as f2:
        while True:
            line = f1.readline().split()
            if not line: break
            word_dict_before[line[0]] = [line[1], line[2]]
        while True:
            line = f2.readline().split()
            if not line: break
            word_dict_after[line[0]] = [line[1], line[2]]

    with open(filename_r_pads, 'r', encoding='utf-8') as f1, open(filename_w_changed, 'w', encoding='utf-8') as f2:
        # p = 0
        while True:
            # if p == 100:
            #     print('hello, time sleep~!')
            #     time.sleep(100)
            line_write = list()
            line = f1.readline().split()
            if not line: break
            for a_word in line:
                if a_word in word_dict_after:
                    line_write.append(a_word)
                    continue
                else:
                    pos = word_dict_before.get(a_word)[0]
                    if pos == 'SL':
                        line_write.append('!#$_ENGLISH')
                    elif pos == 'SN':
                        line_write.append('!#$_NUMBER')
                    elif pos == 'SH':
                        line_write.append('!#$_KANJI_')
                    else:
                        tmp = str('!#$_RARE_' + str(pos))
                        line_write.append(tmp)
            f2.write(' '.join(line_write) + '\n')
            # p += 1

# ==============< Excution >==============================
#
# ========================================================

def attach_pads_start_and_end(filename_r1, filename_w1, filename_w2):
    with open(filename_r1, 'r', encoding='utf-8') as f1, open(filename_w1, 'w', encoding='utf-8') as f3, open(filename_w2, 'w', encoding='utf-8') as f4:
        # p = 0
        while True:
            # if p == pausing_time:
            #     print('hello, time sleep~!~!')
            #     time.sleep(100)
            line1 = f1.readline().split()
            # line2 = f2.readline().split()
            if not line1: break
            line1.insert(0, '!!pad_start')
            # line2.insert(0, 'PAD')
            line1.append('!!pad_end')
            # line2.append('PAD')
            for a_word, a_pos in zip(line1, line2):
                f3.write(a_word + '\t' + a_pos + '\n')
            f4.write(' '.join(line1) + '\n')
            # p += 1

# ==============< Excution >==============================
#
# ========================================================

def words_file_adding_frequency(filename_r, filename_w):
    word_dict = dict()
    with open(filename_r, 'r', encoding='utf-8') as f:
        while True:
            a = f.readline().split()
            if not a: break
            if a[0] in dic:
                dic[a[0]][1] += 1
                continue
            # change values
            dic[a[0]] = [a[1], ]
            # value is list type. so you can use append
            dic[a[0]].append(1)

    tuple = sorted(dic.items())
    # type(tuple)
    # print(len(tuple))
    with open(filename_w, 'w', encoding='utf-8') as f:
        for tmp in tuple:
            tmp = list(tmp)
            c1 = str(tmp[0])
            c2 = str(tmp[1][0])
            c3 = str(tmp[1][1])
            f.write(c1 + '\t' + c2 + '\t' + c3 + '\n')

# ==============< Excution >==============================
#
# ========================================================

def abstract_pos_and_make_pos_list(filename_r, filename_w):
    pos_list = list()
    # read file
    with open(filename_r, 'r', encoding='utf-8') as f:
        data = f.read().split()
        for a_pos in data:
            if a_pos in pos_list:
                continue
            pos_list.append(a_pos)
    with open(filename_w, 'w', encoding='utf-8') as f:
        f.write('\n'.join(pos_list))
