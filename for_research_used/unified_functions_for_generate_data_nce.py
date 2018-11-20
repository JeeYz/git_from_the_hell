# @Author: JayY
# @Date:   2018-11-12T12:07:13+09:00
# @Filename: unified_functions_for_generate_data_nce.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-20T16:46:24+09:00
# @Copyright: JayY


# using "after reducing" file
# using "sents changed" file
#
# making train data file for nce
# ======================================================

import time
import os
import sys
import numpy
sys.setrecursionlimit(10000)

freq_threshold = 8
pausing_time = 10000
num_of_train_data = 51200000
window_size = 5

filename00 = './data/korean_wiki/korean_wiki_result_words_01_after_reducing.txt'
filename01 = './data/korean_wiki/korean_wiki_temp_data_sents_changed.txt'
filename02 = './data/korean_wiki/korean_wiki_result_data_for_training_full_nce.txt'
filename03 = './data/korean_wiki/korean_wiki_result_words_04_adding_index.txt'

filename04 = './data/korean_news/korean_news_result_words_00.txt'
filename05 = './data/korean_news/korean_news_result_sents_00.txt'
filename06 = './data/korean_news/korean_news_result_sents_01.txt'

def checking_between_sents_and_words(temp_word_dict, filename_r, filename_w):
    with open(filename_r, 'r', encoding='utf-8') as f1, open(filename_w, 'w', encoding='utf-8') as f2:
        while True:
            a_line = list()
            line = f1.readline().split()
            if not line: break
            for a_word in line:
                if a_word not in temp_word_dict:
                    print(line, '\t====> word : ', a_word)
                    for_delete_words.append(a_word)
                    a_line.append('for_delete!!')
                else:
                    a_line.append(a_word)
            if 'for_delete!!' not in a_line:
                f2.write(' '.join(a_line) + '\n')

def reducing_low_freq_to_RARE(temp_word_dict, pos_list):
    temp_list_rare_pos = dict()
    for a_pos in pos_list:
        temp_rare = '!@#$_RARE_' + str(a_pos)
        temp_list_rare_pos[str(a_pos)] = temp_rare

    for a_word in temp_word_dict:
        if temp_word_dict[a_word][0] == 'SL':
            temp = temp_word_dict.get('SL')
            if temp not in temp_word_dict:
                temp_word_dict[temp] = ['SL', 1]
            else:
                temp_word_dict[temp][1] += 1
            del temp_word_dict[a_word]
        elif temp_word_dict[a_word][0] == 'SN':
            temp = temp_word_dict.get('SN')
            if temp not in temp_word_dict:
                temp_word_dict[temp] = ['SN', 1]
            else:
                temp_word_dict[temp][1] += 1
            del temp_word_dict[a_word]
        elif temp_word_dict[a_word][0] == 'SH':
            temp = temp_word_dict.get('SH')
            if temp not in temp_word_dict:
                temp_word_dict[temp] = ['SH', 1]
            else:
                temp_word_dict[temp][1] += 1
            del temp_word_dict[a_word]
        elif temp_word_dict[a_word][1] < freq_threshold:
            t_pos = temp_word_dict[a_word][0]
            temp = temp_list_rare_pos.get(t_pos)
            if temp not in temp_word_dict:
                temp_word_dict[temp] = [t_pos, 1]
            else:
                temp_word_dict[temp][1] += 1
            del temp_word_dict[a_word]

    word_dict = temp_word_dict
    return word_dict

def reducing_duplicated_words(filename_r):
    temp_word_dict = dict()
    pos_list = list()
    with open(filename_r, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline().split()
            if not line: break
            if line[1] not in pos_list:
                pos_list.append(line[1])
            if line[0] in temp_word_dict:
                temp_word_dict[line[0]][1] += 1
            else:
                temp_word_dict[line[0]] = [line[1], 1]

        pos_list = sorted(pos_list)
    return temp_word_dict, pos_list

def add_index_to_after_reducing_file(filename_r, filename_w):
    index_num = 0
    with open(filename_r, 'r', encoding='utf-8') as f_r, open(filename_w, 'w', encoding='utf-8') as f_w:
        while True:
            line = f_r.readline().split()
            if not line: break
            f_w.write(str(line[0]) + '\t' + str(line[1]) + '\t' + str(line[2]) + '\t' + str(index_num) + '\n')
            index_num += 1

# add_index_to_after_reducing_file(filename00, filename03)

def make_dict_data(filename_r):
    word_dict = dict()
    index_num = 0
    with open(filename_r, 'r', encoding='utf-8') as f_r:
        while True:
            line = f_r.readline().split()
            if not line: break
            word_dict[line[0]] = list([index_num, line[1], line[2]])
            index_num += 1
    return word_dict

# word_dict = make_dict_data(filename00)

def generate_train_data(word_dict, filename_r, filename_w):
    with open(filename_r, 'r', encoding='utf-8') as f_r, open(filename_w, 'w', encoding='utf-8') as f_w:
        temp_num = 0
        # p = 0
        while True:
            # if p == 100:
            #     print('hello, time sleep~!~!')
            #     time.sleep(pausing_time)
            line = f_r.readline().split()
            if not line: break
            num = len(line) - 1
            for center_word in range(1, num):
                if center_word >= window_size:
                    start_num = center_word - window_size
                    if center_word+window_size > num:
                        end_num = num + 1
                    else:
                        end_num = center_word + window_size + 1
                else:
                    start_num = 0
                    if center_word+window_size > num:
                        end_num = num + 1
                    else:
                        end_num = center_word + window_size + 1
                for target_word in range(start_num, end_num):
                    center_idx = word_dict.get(line[center_word])[0]
                    target_idx = word_dict.get(line[target_word])[0]
                    f_w.write(str(center_idx) + '\t' + str(target_idx) + '\n')
            if temp_num%1000 == 0:
                print('hello, world', '\t', temp_num)
            temp_num += 1
            # p += 1

# generate_train_data(word_dict, filename01, filename02)

dir_path00 = './data/korean_wiki/train_data_nce/'
dir_path01 = './data/korean_news/train_data_nce/'

def dividing_full_train_data_file(filename_r, dir_path):
    filename_to_write = 'korean_wiki_train_data_for_nce_'
    file_ext = '.txt'
    with open(filename_r, 'r', encoding='utf-8') as f_r:
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
        line_para_num = 0
        file_num_para = 0
        while_switch = 1
        while while_switch:
            filename_w = dir_path + filename_to_write + str('%03d' % file_num_para) + file_ext
            with open(filename_w, 'w', encoding='utf-8') as f_w:
                while True:
                    line = f_r.readline().split()
                    if not line:
                        while_switch = 0
                        break
                    if line_para_num == num_of_train_data:
                        line_para_num = 0
                        break
                    f_w.write(str(line[0]) + '\t' + str(line[1]) + '\n')
                    line_para_num += 1
                file_num_para += 1
            print('hello, world~!~! well done for generating a file')

# dividing_full_train_data_file(filename02, dir_path)
