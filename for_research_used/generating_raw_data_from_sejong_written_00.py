# @Author: JayY
# @Date:   2018-08-13T11:20:44+09:00
# @Filename: new_10.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T17:15:12+09:00
# @Copyright: JayY

# @new_10.py

'''
extract words from file
This file is completed!!
'''
# @@ output result in a file
fout = open("temp_result.txt", 'w', encoding='utf-8')

# @@ target file
with open("BTAA0155.txt", encoding = 'utf-8') as fin:
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
            fout.write(w + '\t' + t + '\n')
            continue

        b = i.split('/')
        w = b[0]
        t = b[1]
        fout.write(w + '\t' + t + '\n')

fout.close()
