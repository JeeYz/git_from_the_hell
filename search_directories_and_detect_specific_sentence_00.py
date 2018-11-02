# @Author: JayY <JeeYz>
# @Date:   2018-10-30T09:53:24+09:00
# @Filename: search_directories_and_detect_specific_sentence_00.py
# @Last modified by:   JeeYz
# @Last modified time: 2018-11-02T14:00:17+09:00
# @Copyright: JayY



import os

for (path, dir, files) in os.walk('d:/Project-NLP/현대문어_형태분석_말뭉치'):
    for filename1 in files:
        print(path, '\t', dir, '\t', filename1)
'''
for (path, dir, files) in os.walk('d:/Project-NLP/현대문어_형태분석_말뭉치'):
    for filename2 in files:
        if '.txt' in filename2:
            with open(path+'/'+filename2, 'r', encoding='utf-8') as f:
                while True:
                    line = f.readline()
                    if not line: break
                    if '병신' in line or "도없는" in line:
                        print(line)
'''

with open('changed_sentence_data_01.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line: break
        if '병신' in line and '없' in line:
            print(line)
