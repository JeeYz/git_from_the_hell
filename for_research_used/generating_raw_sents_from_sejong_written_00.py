# @Author: JayY
# @Date:   2018-10-22T16:02:15+09:00
# @Filename: make_train_data_sentence_01.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T14:15:13+09:00
# @Copyright: JayY

# @ make change data with !#$_RARE words

fw = open('korean_wiki_result_sents_01.txt', 'w', encoding='utf-8')
# all sentences are changed with !#$_RARE words. and output to this file

word_dict = dict()
frequency_threshold = 8

with open('korean_wiki_result_words_02.txt', 'r', encoding='utf-8') as f:
# this file's structure
# word \t type(pos) \t frequency \n
# ======================================
    line = f.read().split()
    for i in range(len(line)//3):
        word_dict[line[i*3]] = [line[i*3 + 1], int(line[i*3 + 2])]

with open('korean_wiki_result_sents_00.txt', 'r', encoding='utf-8') as f:
# read from this file before sentences
    data = f.read().split()
    for word in data:
        if word not in word_dict:
            continue
        if word_dict[word][0] == 'SL':
            fw.write('!#$_ENGLISH' + ' ')
        elif word_dict[word][0] == 'SN':
            fw.write('!#$_NUMBER' + ' ')
        elif word_dict[word][0] == 'SH':
            fw.write('!#$_KANJI_' + ' ')
        elif word_dict[word][1] < frequency_threshold:
            fw.write(str('!#$_RARE_' + word_dict[word][0] + ' '))
        else:
            fw.write(str(word))
            fw.write(str(' '))
        if word == 'pad_s_001':
            fw.write('\n')
