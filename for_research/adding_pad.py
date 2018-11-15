# @Author: JayY
# @Date:   2018-11-07T13:10:54+09:00
# @Filename: adding_pad.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-07T14:07:19+09:00
# @Copyright: JayY

import time

pausing_time = 200

filename1 = './data/korean_wiki/korean_wiki_raw_data_words.txt'
filename2 = './data/korean_wiki/korean_wiki_raw_data_poses.txt'
filename3 = './data/korean_wiki/korean_wiki_temp_data_words.txt'
filename4 = './data/korean_wiki/korean_wiki_temp_data_sents_adding_pad.txt'

with open(filename1, 'r', encoding='utf-8') as f1, open(filename2, 'r', encoding='utf-8') as f2, open(filename3, 'w', encoding='utf-8') as f3, open(filename4, 'w', encoding='utf-8') as f4:
    # p = 0
    while True:
        # if p == pausing_time:
        #     print('hello, time sleep~!~!')
        #     time.sleep(100)
        line1 = f1.readline().split()
        line2 = f2.readline().split()
        if not line1: break
        line1.insert(0, '!!pad_start')
        line2.insert(0, 'PAD')
        line1.append('!!pad_end')
        line2.append('PAD')
        for a_word, a_pos in zip(line1, line2):
            f3.write(a_word + '\t' + a_pos + '\n')
        f4.write(' '.join(line1) + '\n')
        # p += 1
