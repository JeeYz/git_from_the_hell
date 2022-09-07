# @Author: JayY
# @Date:   2018-11-05T12:05:23+09:00
# @Filename: generate_data_from_kowiki_00.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-21T13:56:41+09:00
# @Copyright: JayY

# ==============<  >===============================
# this is for news data
#
# =================================================

import os

# number_of_files = 25757

# fres1 = open('korean_wiki_result_words_00.txt', 'w', encoding='utf-8')
# fres2 = open('korean_wiki_result_sents_00.txt', 'w', encoding='utf-8')
# fres1 = open('korean_news_result_words_00.txt', 'w', encoding='utf-8')
# fres2 = open('korean_news_result_sents_00.txt', 'w', encoding='utf-8')

filename00 = './data/korean_news/korean_news_result_sents_00.txt'
filename01 = './data/korean_news/korean_news_result_poses_00.txt'

# common_path1 = 'd:/Project-NLP/korean_wiki/lem/'
# common_path2 = 'd:/Project-NLP/korean_wiki/pos/'
common_path1 = 'd:/Project-NLP/ETRI_NEWS_DATA/lem/'
common_path2 = 'd:/Project-NLP/ETRI_NEWS_DATA/pos/'

name_lem = 'input_kowiki_remdoctag_'
name_pos = 'input_kowiki_remdoctag_'
ext_lem = '.lem'
ext_pos = '.pos'

if os.path.isdir('./data/korean_news/') == False:
    os.mkdir('./data/korean_news/')

lem_file_list = list()
pos_file_list = list()
word_dict = dict()

for (path, dir, files) in os.walk(common_path1):
    for filename in files:
        if '20180101' in filename:
            continue
        if '.lem' in filename:
            filename = path + '/' + filename
            lem_file_list.append(filename)

for (path, dir, files) in os.walk(common_path2):
    for filename in files:
        if '20180101' in filename:
            continue
        if '.pos' in filename:
            filename = path + '/' + filename
            pos_file_list.append(filename)

# print(lem_file_list)
# print(pos_file_list)

f_log = open('incorrect_lines_korean_news.txt', 'w', encoding='utf-8')

with open(filename00, 'w', encoding='utf-8') as f1, open(filename01, 'w', encoding='utf-8') as f2:
    wrong_count = 0
    for lem_file, pos_file in zip(lem_file_list, pos_file_list):
        with open(lem_file, 'r', encoding='utf-8') as f3, open(pos_file, 'r', encoding='utf-8') as f4:
            while True:
                # line1 = f3.readline().split()
                # line2 = f4.readline().split()
                line_t = f3.readline()
                line2 = f4.readline().split()
                line1 = line_t.split()
                if not line1: break
                if len(line1) != len(line2):
                    continue
                    # f_log.write(str(lem_file) + '\n')
                    # f_log.write(' '.join(line1) + '=====>>>>>' + str(len(line1)) + '# of line:' + str(wrong_count) + '\n')
                    # f_log.write(' '.join(line2) + '=====>>>>>' + str(len(line2)) + '\t\t# of line:' + str(wrong_count) + '\n\n\n')
                    # print(line1, '=====>>>>>', str(len(line1)))
                    # print(line2, '=====>>>>>', str(len(line2)))
                    # print('#of line:', wrong_count, '\n\n\n')
                    # wrong_count += 1
                if '[이상/NNG' in line2 or '되/VV]' in line2:
                    for a_word in line2:
                        if a_word == '[이상/NNG':
                            a_word = 'NNG'
                        elif a_word == '되/VV]':
                            a_word = 'VV'
                # f1.write(' '.join(line1))
                # f2.write(' '.join(line2))
                for i in range(len(line1)):
                    input1 = line1[i] + '\t' + line2[i] + '\n'
                    f1.write(str(input1))
                f2.write(line_t)
        print("hello, world~!  ", lem_file, " is done!!")

f_log.close()

#
# for num in range(number_of_files):
#     filename_lem = common_path1 + name_lem + str("%05d" % num) + ext_lem
#     filename_pos = common_path2 + name_pos + str("%05d" % num) + ext_pos
#     fp1 = open(filename_lem, 'r', encoding='utf-8')
#     fp2 = open(filename_pos, 'r', encoding='utf-8')
#     while True:
#         line_t = fp1.readline()
#         line2 = fp2.readline().split()
#         line1 = line_t.split()
#         if not line1: break
#         for i in range(len(line1)):
#             input1 = line1[i] + '\t' + line2[i] + '\n'
#             fres1.write(str(input1))
#         fres2.write(line_t)
#     fp1.close()
#     fp2.close()
#     print("hello, world~!  ", filename_lem, " is done!!")
