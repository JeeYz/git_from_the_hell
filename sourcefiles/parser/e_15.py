# @Author: JY
# @Date:   2019-01-30T16:34:46+09:00
# @Filename: e_15.py
# @Last modified by:   JY
# @Last modified time: 2019-01-30T16:42:08+09:00
# @Copyright: JeeY



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

filename04 = './data/korean_news/korean_news_result_words_05.txt'
filename05 = './data/korean_news/korean_news_result_sents_03.txt'
filename06 = './data/korean_news/korean_news_data_for_training_full_nce.txt'

filename07 = 'result_raw_words_list_temp_with_freq_1.words'
filename08 = 'result_temp_sentence_01.sentence'
filename09 = 'ETRI_parsing_full_train_data.traindata'

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
    with open(filename_r, 'r', encoding='utf-8') as f_r:
        while True:
            line = f_r.readline().split()
            if not line: break
            word_dict[line[0]] = list([int(line[1]), line[2], int(line[3])])
    return word_dict

word_dict = make_dict_data(filename07)

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

generate_train_data(word_dict, filename08, filename09)

# dir_path00 = './'
# dir_path01 = './'

# def dividing_full_train_data_file(filename_r, dir_path):
#     filename_to_write = 'korean_news_train_data_for_nce_'
#     file_ext = '.txt'
#     with open(filename_r, 'r', encoding='utf-8') as f_r:
#         if not os.path.isdir(dir_path):
#             os.mkdir(dir_path)
#         line_para_num = 0
#         file_num_para = 0
#         while_switch = 1
#         while while_switch:
#             filename_w = dir_path + filename_to_write + str('%03d' % file_num_para) + file_ext
#             with open(filename_w, 'w', encoding='utf-8') as f_w:
#                 while True:
#                     line = f_r.readline().split()
#                     if not line:
#                         while_switch = 0
#                         break
#                     if line_para_num == num_of_train_data:
#                         line_para_num = 0
#                         break
#                     f_w.write(str(line[0]) + '\t' + str(line[1]) + '\n')
#                     line_para_num += 1
#                 file_num_para += 1
#             print('hello, world~!~! well done for generating a file')

# dividing_full_train_data_file(filename09, dir_path01)










## endl
