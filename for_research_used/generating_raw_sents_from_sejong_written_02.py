# @Author: JayY
# @Date:   2018-10-22T15:50:21+09:00
# @Filename: search_directories_and_make_sentence_file_01.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-07T10:27:01+09:00
# @Copyright: JayY



import os

fw = open('result_sent_02.txt', 'w', encoding='utf-8')

for (path, dir, files) in os.walk("d:/Project-NLP/현대문어_형태분석_말뭉치/"):
    for filenames in files:
        with open(path+filenames, 'r', encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line: break
                if '<p>\n' in line or '<head>\n' in line or '<date>\n' in line:
                    c = ""
                    while True:
                        a = f.readline()
                        if not a: break
                        if '</p>' in a: break
                        if '</head>' in a: break
                        if '</date>' in a: break
                        a = a.split()
                        b = a[2:]
                        for t in b:
                            if '+' is t: continue
                            t = t.split('/')[0]
                            c = c + t + ' '
                    fw.write('pad_s_000' + ' ' + c + ' ' + 'pad_s_001' + '\n')
