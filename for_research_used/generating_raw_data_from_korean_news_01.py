# @Author: JayY
# @Date:   2018-11-20T16:06:02+09:00
# @Filename: generating_raw_data_from_korean_news_01.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-21T11:06:31+09:00
# @Copyright: JayY



# ============< NOTICE >==============================
# this is failure case.
# too complex.
# "simple is better than complex"
# remind myself when i make program
# ====================================================

import time
import os
import sys
import numpy
sys.setrecursionlimit(10000)

freq_threshold = 8
pausing_time = 10000
num_of_train_data = 51200000
window_size = 5
#
# filename00 = './data/korean_wiki/korean_wiki_result_words_01_after_reducing.txt'
# filename01 = './data/korean_wiki/korean_wiki_temp_data_sents_changed.txt'
# filename02 = './data/korean_wiki/korean_wiki_result_data_for_training_full_nce.txt'
# filename03 = './data/korean_wiki/korean_wiki_result_words_04_adding_index.txt'

# filename04 = './data/korean_news/korean_news_result_words_00.txt'
filename05 = './data/korean_news/korean_news_result_sents_00.txt'
filename06 = './data/korean_news/korean_news_result_sents_01.txt'
filename07 = './data/korean_news/korean_news_result_words_01.txt'
filename08 = './data/korean_news/korean_news_result_words_02.txt'
filename09 = './data/korean_news/korean_news_result_poses_list.txt'
filename10 = './data/korean_news/korean_news_result_sents_02.txt'
filename08 = './data/korean_news/korean_news_result_words_03.txt'


def replace_rare_words_to_RARE(filename_r, filename_w, word_dict, temp_list_rare_pos):
    with open(filename_r, 'r', encoding='utf-8') as f1, open(filename_w, 'w', encoding='utf-8') as f2:
        while True:
            line = f1.readline().split()
            if not line:break
            new_line = list()
            for a_word in line:
                if a_word in word_dict:
                    new_line.append(a_word)
                else:
                    temp = temp_list_rare_pos.get(word_dict[a_word][1])
                    new_line.append(temp)
            f2.write(' '.join(new_line) + '\n')

def count_number_of_sents(filename_r):
    para = 0
    with open(filename_r, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line: break
            para += 1
    num_of_sents = para
    return num_of_sents

def write_file_words_01(filename_w, word_dict, num_of_sents):
    word_dict['!@#$pad_start'] = ['PAD', num_of_sents]
    word_dict['!@#$pad_end'] = ['PAD', num_of_sents]
    temp_tuple = sorted(word_dict.items())
    word_dict.clear()
    index_para = 0
    for a_tuple in temp_tuple:
        new_word_dict[a_tuple[0]] = [index_para, a_tuple[1], a_tuple[2]]
    with open(filename_w, 'w', encoding='utf-8') as f:
        for a_word in new_word_dict:
            a_line = str(a_word) + '\t' + str(word_dict[a_word][0]) + '\t' + str(word_dict[a_word][1]) + '\t' + str(word_dict[a_word][2])
            f.write(a_line + '\n')
    return word_dict

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
                f2.write('#$pad_start' + ' ' + ' '.join(a_line) + ' ' + '#$pad_end' +'\n')

def reducing_low_freq_to_RARE(temp_word_dict, pos_list):
    temp_list_rare_pos = dict()
    for a_pos in pos_list:
        temp_rare = '!@#$_RARE_' + str(a_pos)
        temp_list_rare_pos[str(a_pos)] = temp_rare

    for_delete_list = list()
    for a_word in temp_word_dict:
        if temp_word_dict[a_word][0] == 'SL':
            temp = temp_list_rare_pos.get('SL')
            if temp in temp_word_dict:
                temp_word_dict[temp][1] += 1
            else:
                temp_word_dict[temp] = ['SL', 1]
            for_delete_list.append(a_word)
        elif temp_word_dict[a_word][0] == 'SN':
            temp = temp_list_rare_pos.get('SN')
            # print(temp)
            if temp in temp_word_dict:
                temp_word_dict[temp][1] += 1
            else:
                temp_word_dict[temp] = ['SN', 1]
            for_delete_list.append(a_word)
        elif temp_word_dict[a_word][0] == 'SH':
            temp = temp_list_rare_pos.get('SH')
            if temp in temp_word_dict:
                temp_word_dict[temp][1] += 1
            else:
                temp_word_dict[temp] = ['SH', 1]
            for_delete_list.append(a_word)
        elif temp_word_dict[a_word][1] < freq_threshold:
            t_pos = temp_word_dict[a_word][0]
            temp = temp_list_rare_pos.get(t_pos)
            if temp not in temp_word_dict:
                temp_word_dict[temp][1] += 1
            else:
                temp_word_dict[temp] = [t_pos, 1]
            for_delete_list.append(a_word)

    for del_word in for_delete_list:
        del temp_word_dict[del_word]

    word_dict = temp_word_dict
    return word_dict, temp_list_rare_pos

def make_dictionary_for(filename_r1, filename_r2):
    temp_word_dict = dict()
    pos_list = list()
    with open(filename_r1, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline().split()
            if not line: break
            if line[0] in temp_word_dict:
                temp_word_dict[line[0]][1] += 1
            else:
                temp_word_dict[line[0]] = [line[1], 1]

    with open(filename_r1, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline().split()
            if not line: break
            pos_list.append(line)

    return temp_word_dict, pos_list


def main():
    temp_word_dict, pos_list = make_dictionary_for(filename07, filename09)
    # checking_between_sents_and_words(temp_word_dict, filename05, filename06)
    word_dict, temp_list_rare_pos = reducing_low_freq_to_RARE(temp_word_dict, pos_list)
    num_of_sents = count_number_of_sents(filename06)
    word_dict = write_file_words_01(filename08, word_dict, num_of_sents)
    replace_rare_words_to_RARE(filename06, filename10, word_dict, temp_list_rare_pos)


if __name__  == "__main__":
    main()
