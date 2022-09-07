# @Author: JayY
# @Date:   2018-11-21T13:56:53+09:00
# @Filename: generating_raw_data_from_korean_news_04.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-22T10:11:46+09:00
# @Copyright: JayY


import time

freq_threshold = 8

filename00 = './data/korean_news/korean_news_result_words_04.txt'
filename01 = './data/korean_news/korean_news_result_words_05.txt'
filename02 = './data/korean_news/korean_news_result_poses_list.txt'

def reducing_low_freq_words(filename_r1, filename_r2, filename_w):
    pos_list = list()
    pos_dict = dict()
    with open(filename_r2, 'r', encoding='utf-8') as f:
        pos_list = f.read().split()
        for pos in pos_list:
            pos_dict[pos] = '##RARE_' + str(pos)
    # print(pos_dict)
    pos_list.clear()
    word_dict = dict()
    with open(filename_r1, 'r', encoding='utf-8') as f1, open(filename_w, 'w', encoding='utf-8') as f2:
        while True:
            line = f1.readline().split()
            if not line: break
            if str(line[1]) == 'SL':
                if '##RARE_SL' in word_dict:
                    word_dict['##RARE_SL'][1] += 1
                else:
                    word_dict['##RARE_SL'] = ['SL', 1]
            elif str(line[1]) == 'SN':
                if '##RARE_SN' in word_dict:
                    word_dict['##RARE_SN'][1] += 1
                else:
                    word_dict['##RARE_SN'] = ['SN', 1]
            elif str(line[1]) == 'SH':
                if '##RARE_SH' in word_dict:
                    word_dict['##RARE_SH'][1] += 1
                else:
                    word_dict['##RARE_SH'] = ['SH', 1]
            elif int(line[2]) < freq_threshold:
                temp = str(pos_dict.get(str(line[1])))
                if  temp in word_dict:
                    word_dict[temp][1] += 1
                else:
                    word_dict[temp] = ['SH', 1]
            else:
                if str(line[0]) in word_dict:
                    if '##RARE_SH' in word_dict:
                        print('hello, Kanji~!~!~! ----> ', word_dict.get('##RARE_SH'))
                    print('hello, error~!!', line, '\t', word_dict.get('None'))
                    # print(word_dict)
                    time.sleep(100000)
                else:
                    word_dict[str(line[0])] = [str(line[1]), str(line[2])]

        print('hello, world~!~!')
        voca_tuple = sorted(word_dict.items())
        word_dict.clear()
        index_para = 0
        for (key, value) in voca_tuple:
            f2.write(str(key) + '\t' + str(index_para) + '\t' + str(value[0]) + '\t' + str(value[1]) + '\n')
            index_para += 1

reducing_low_freq_words(filename00, filename02, filename01)
