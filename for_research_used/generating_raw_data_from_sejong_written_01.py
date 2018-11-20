# @Author: JayY
# @Date:   2018-10-18T10:46:59+09:00
# @Filename: search_directory_and_make_full_data_file_01.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-08T09:39:33+09:00
# @Copyright: JayY



######################################################################
# search directory and make full data file
# above all, search every directory
# after then, make a full data file
######################################################################

import os
with open('types_abstracts.txt', 'r', encoding='utf-8') as f:
    t_list = f.read().split()
fout = open("temp_result.txt", 'w', encoding='utf-8')

t_a = dict()
for (path, dir, files) in os.walk("d:/Project-NLP/현대문어_형태분석_말뭉치/"):
    for filenames in files:
        with open(path+filenames, 'r', encoding='utf-8') as fin:
            a = fin.read()
            for i in a.split():
                if i[0] == '/' or i[-1] == '/':
                    continue
                if i == '<head>' or i == '<date>' or i == '<p>':
                    fout.write('pad_s_000' + '\t' + 'PAD' + '\n')
                    fout.write('pad_s_001' + '\t' + 'PAD' + '\n')
                    continue
                if i is '+':
                    continue
                if 'BTAA' in i:
                    continue
                if '<' in i and '>' in i:
                    continue
                if '/' not in i:
                    continue
                if i is '/':
                    continue
                if '-00' in i:
                    continue
                if '/01/' in i or '/02/' in i or '/03/' in i or '/04/' in i or '/05/' in i or '/06/' in i:
                    continue
                if '/07/' in i or '/08/' in i or '/09/' in i or '/10/' in i or '/11/' in i or '/12/' in i:
                    continue
                if '//' in i:
                    w = i[0]
                    t = i[2:]
                    if t not in t_list:
                        continue
                    fout.write(w + '\t' + t + '\n')
                    continue

                b = i.split('/')
                w = b[0]
                t = b[1]
                if 'A' <= t and t <= 'ZZZZ':
                    if t in t_list:
                        fout.write(w + '\t' + t + '\n')

fout.close()
