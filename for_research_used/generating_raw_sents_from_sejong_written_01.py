# @Author: JayY
# @Date:   2018-09-18T09:13:17+09:00
# @Filename: new_26.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T13:57:39+09:00
# @Copyright: JayY

# @ new_26.py

###############################################################
# make file for sentences of training
# from raw file
# making full sentences for training
###############################################################
import os

fw = open('result_sent_01.txt', 'w', encoding='utf-8')

with open('BTAA0001.txt', 'r', encoding='utf-8') as f:
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
