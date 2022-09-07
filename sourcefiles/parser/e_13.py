# @Author: JY
# @Date:   2019-01-30T11:40:27+09:00
# @Filename: e_13.py
# @Last modified by:   JY
# @Last modified time: 2019-01-30T15:06:07+09:00
# @Copyright: JeeY

filename00 = 'd:/Programming/Language_Model/data/korean_wiki/korean_wiki_result_words_01_after_reducing.txt'


with open(filename00, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line: break
        print(line)



## endl
