# @Author: JayY
# @Date:   2018-11-07T15:07:06+09:00
# @Filename: change_sentence_using_reduced_words.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-07T15:48:24+09:00
# @Copyright: JayY

import time
import copy

filename0 = './data/korean_wiki/korean_wiki_result_words_00_before_reducing.txt'
filename1 = './data/korean_wiki/korean_wiki_result_words_01_after_reducing.txt'
filename2 = './data/korean_wiki/korean_wiki_temp_data_sents_adding_pad.txt'
filename3 = './data/korean_wiki/korean_wiki_temp_data_sents_changed.txt'

word_dict_before = dict()
word_dict_after = dict()

with open(filename0, 'r', encoding='utf-8') as f1, open(filename1, 'r', encoding='utf-8') as f2:
    while True:
        line = f1.readline().split()
        if not line: break
        word_dict_before[line[0]] = [line[1], line[2]]
    while True:
        line = f2.readline().split()
        if not line: break
        word_dict_after[line[0]] = [line[1], line[2]]

with open(filename2, 'r', encoding='utf-8') as f1, open(filename3, 'w', encoding='utf-8') as f2:
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
