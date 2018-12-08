# @Author: JayY
# @Date:   2018-11-05T14:02:53+09:00
# @Filename: show_inside_file.py
# @Last modified by:   JayY
# @Last modified time: 2018-12-08T10:57:54+09:00
# @Copyright: JayY

# it is just for show inside file
# because some files are too big to read
# I will check the file well made or not
# and several checking by these functions of the file
# =======================================================


import time
import copy
import os

data_dir_path = 'd:/Programming/Language_Model'

filename00 = 'd:/Programming/Language_Model/data/korean_wiki/korean_wiki_raw_data_words.txt'
filename01 = 'd:/Programming/Language_Model/data/korean_wiki/korean_wiki_raw_data_poses.txt'
filename02 = 'd:/Programming/Language_Model/data/korean_wiki/korean_wiki_result_words_00.txt'

filename_pos = 'd:/Programming/Language_Model/data/korean_wiki/abstracted_pos_list.txt'

filename03 = 'd:/Programming/Language_Model/data/korean_wiki/korean_wiki_result_words_02_huff_words.txt'
filename04 = 'd:/Programming/Language_Model/data/korean_wiki/korean_wiki_result_words_02_huff_nodes.txt'
filename05 = 'd:/Programming/Language_Model/data/korean_wiki/korean_wiki_result_data_for_training_full.txt'
filename06 = 'd:/Programming/Language_Model/data/korean_wiki/korean_wiki_result_data_for_training_full_nce.txt'

filename07 = 'd:/Programming/Language_Model/data/korean_news/korean_news_result_words_00.txt'
filename08 = 'd:/Programming/Language_Model/data/korean_news/korean_news_result_sents_00.txt'
filename09 = 'd:/Programming/Language_Model/data/korean_news/korean_news_result_words_01.txt'
filename10 = 'd:/Programming/Language_Model/data/korean_news/korean_news_result_words_02.txt'
filename11 = 'd:/Programming/Language_Model/data/korean_news/korean_news_result_words_05.txt'

filename12 = 'd:/Programming/Language_Model/data/korean_news/korean_news_data_for_training_full_nce.txt'

filename13 = 'd:/Programming/Language_Model/data/sejong/written/changed_sentence_Data_01.txt'
filename14 = 'd:/Programming/Language_Model/data/sejong/written/result_11.txt'

filename15 = 'd:/Programming/Language_Model/data/korean_wiki/korean_wiki_result_words_00_before_reducing.txt'
filename16 = 'd:/Programming/Language_Model/data/korean_wiki/korean_wiki_temp_data_sents_adding_pad.txt'

filename17 = 'd:/Programming/Language_Model/data/korean_news/korean_news_result_sents_03.txt'
filename18 = 'd:/Programming/Language_Model/data/korean_news/korean_news_result_words_04.txt'




def checking_words_lines(filename_r):
    with open(filename_r, 'r', encoding='utf-8') as f:
        line_para = 0
        while True:
            line = f.readline().split()
            if not line:break
            # if len(line) != 4:
            #     print(line, '\t', line_para)
            line_para += 1
        print(line_para)
#============**** excution ****===============
checking_words_lines(filename17)
# ============================================

def checking_word(filename_r):
    with open(filename_r, 'r', encoding='utf-8') as f:
        line_para = 0
        while True:
            line = f.readline().split()
            # print(line, '\t', line_para)
            if not line:break
            if line[0] == '##pad_start':
                print('hello, world~! ----> ', line_para, '\t', line)
                # time.sleep(10000)
            line_para += 1
        print(line_para)

#============**** excution ****===============
# checking_word(filename10)
# ============================================

def checking_lines(filename_r):
    with open(filename_r, 'r', encoding='utf-8') as f:
        line_para = 0
        pausing_lines = 100
        pos_list = list()
        while True:
            line = f.readline().split()
            if not line: break
            if line[1] not in pos_list:
                pos_list.append(line[1])
            if len(line) != 2:
                print(line)
        pos_list = sorted(pos_list)
        print(pos_list)

#============**** excution ****===============
# checking_lines(filename07)
# ============================================

def read_files(filename_r):
    with open(filename_r, 'r', encoding='utf-8') as f:
        line_para = 0
        pausing_lines = 100
        while True:
            line = f.readline()
            if not line: break
            print(line)
            if line_para == pausing_lines:
                print("hello, time sleep~!")
                time.sleep(10000)
            line_para += 1

#============**** excution ****===============
# read_files(filename07)
# read_files(filename17)
# ============================================

def checking_number_of_files(filename_r1, filename_r2):
    with open(filename_r1, 'r', encoding='utf-8') as f1, open(filename_r2, 'r', encoding='utf-8') as f2:
        while True:
            line1 = f1.readline().split()
            line2 = f2.readline().split()
            if not line1: break
            if len(line1) != len(line2):
                print(line1)
                print(line2)
                print('===========================')

#============**** excution ****===============
# checking_number_of_files(filename07, filename08)
# ============================================

def check_train_data_file_nce(filename_r):
    with open(filename_r, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline().split()
            if not line: break
            if len(line) != 2:
                print('hello, world~! incorrect line!!')

#============**** excution ****===============
# check_train_data_file_nce(filename06)
# ============================================

def count_lines_of_file(filename_r):
    count = 0
    with open(filename_r, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line: break
            count += 1
    print('total number of lines: ', count)

#============**** excution ****===============
# count_lines_of_file(filename08)
# ============================================

def checking_well_made_or_not(filename_r):
    with open(filename_r, 'r', encoding='utf-8') as f:
        linepara = 0
        while True:
            line = f.readline().split()
            if not line: break
            if len(line) != 3:
                print('hello, world~!')
                print(line, '\t', '# of line=', linepara)
            else:
                if line[2] != '0' and line[2] != '1':
                    print('hello, world@!@!@!')
                    print(line, '\t', '# of line=', linepara)
            linepara += 1


#============**** excution ****===============
# checking_well_made_or_not(filename05)
# ============================================

def checking_correctness(filename):
    pos_list = list()
    with open(filename_pos, 'r', encoding='utf-8') as f:
        pos_list = f.read().split()
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline().split()
            if not line: break
            if line[1] not in pos_list:
                print('hello, time sleep~!~!')
                print(line)
                time.sleep(100)

#============**** excution ****===============
# checking_correctness(filename02)
# ============================================

def change_raw_data_file(filename):
    filename_tmp = './data/korean_wiki/korean_wiki_raw_data_poses_tmp.txt'
    with open(filename, 'r', encoding='utf-8') as f1, open(filename_tmp, 'w', encoding='utf-8') as f2:
        # para = 0
        while True:
            # if para == 100:
            #     print('hello, time sleep~!~!')
            #     time.sleep(100)
            line = f1.readline().split()
            if not line: break
            if '[이상/NNG' in line or '되/VV]' in line:
                new_line = list()
                for a_word in line:
                    if a_word == '[이상/NNG':
                        new_line.append('NNG')
                        continue
                    elif a_word == '되/VV]':
                        new_line.append('VV')
                        continue
                    new_line.append(a_word)
                line = copy.deepcopy(new_line)
            wirte_line = ' '.join(line)
            f2.write(wirte_line + '\n')
            # para += 1

#============**** excution ****===============
# change_raw_data_file(filename01)
# ============================================


def detecting_specific_sentence(filename1, filename2):
    with open(filename1, 'r', encoding='utf-8') as f1, open(filename2, 'r', encoding='utf-8') as f2:
        while True:
            line1 = f1.readline()
            line2 = f2.readline()
            if not line1: break
            if '[이상/NNG' in line2 or '되/VV' in line2:
                print(line1)
                print(line2)

#============**** excution ****===============
# detecting_specific_sentence(filename00, filename01)
# ============================================


def showing_inside_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:break
            print(line)
            # if "None" in line:
            #     print(line)


#============**** excution ****===============
# showing_inside_file(filename11)
# ============================================
