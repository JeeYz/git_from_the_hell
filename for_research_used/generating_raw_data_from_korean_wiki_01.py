# @Author: JayY
# @Date:   2018-11-07T10:47:05+09:00
# @Filename: make_one_file_from_raw_data.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-07T11:03:16+09:00
# @Copyright: JayY

import os
import time

fp1 = open('./data/korean_wiki/korean_wiki_raw_data_words.txt', 'w', encoding='utf-8')
fp2 = open('./data/korean_wiki/korean_wiki_raw_data_poses.txt', 'w', encoding='utf-8')

for (path, dir, files) in os.walk('d:/Project-NLP/korean_wiki/'):
    for filename in files:
        if ".lem" in filename:
            filename1 = path + '/' + filename
            with open(filename1, 'r', encoding='utf-8') as f:
                # para = 0
                while True:
                    # if para == 100:
                    #     print('hello, time pause~!')
                    #     time.sleep(30)
                    line = f.readline().split()
                    if not line: break
                    a = ' '.join(line)
                    fp1.write(a + '\n')
                    # para += 1
        elif ".pos" in filename:
            filename2 = path + '/' + filename
            with open(filename2, 'r', encoding='utf-8') as f:
                # para = 0
                while True:
                    # if para == 100:
                    #     print('hello, time pause~!')
                    #     time.sleep(30)
                    line = f.readline().split()
                    if not line: break
                    a = ' '.join(line)
                    fp2.write(a + '\n')
                    # para += 1
