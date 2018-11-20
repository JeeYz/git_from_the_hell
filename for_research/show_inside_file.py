# @Author: JayY
# @Date:   2018-11-05T14:02:53+09:00
# @Filename: show_inside_file.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-16T16:51:25+09:00
# @Copyright: JayY

# it is just for show inside file
# because some files are too big to read
# I will check the file well made or not
# and several checking by these functions of the file
# =======================================================


import time
import copy
import os

filename00 = './data/korean_wiki/korean_wiki_raw_data_words.txt'
filename01 = './data/korean_wiki/korean_wiki_raw_data_poses.txt'
filename02 = './data/korean_wiki/korean_wiki_result_words_00.txt'

filename_pos = './data/korean_wiki/abstracted_pos_list.txt'

filename03 = './data/korean_wiki/korean_wiki_result_words_02_huff_words.txt'
filename04 = './data/korean_wiki/korean_wiki_result_words_02_huff_nodes.txt'
filename05 = './data/korean_wiki/korean_wiki_result_data_for_training_full.txt'
filename06 = './data/korean_wiki/korean_wiki_result_data_for_training_full_nce.txt'

filename07 = './data/korean_news/korean_news_result_sents_00.txt'
filename08 = './data/korean_news/korean_news_result_poses_00.txt'



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

# checking_number_of_files(filename07, filename08)

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
# count_lines_of_file(filename05)
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


def checking_files_of_huff():
    pass

#============**** excution ****===============
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
            print(line)
            if 'pad_s_000' in line:
                print(line)

#============**** excution ****===============
# showing_inside_file(filename05)
# ============================================

# checking_correctness(filename02)
