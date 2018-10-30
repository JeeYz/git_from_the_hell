
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
