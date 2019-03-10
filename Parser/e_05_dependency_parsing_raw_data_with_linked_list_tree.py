# @Author: JY
# @Date:   2019-01-25T11:21:08+09:00
# @Filename: e_5.py
# @Last modified by:   JY
# @Last modified time: 2019-01-28T13:24:26+09:00
# @Copyright: JeeY


# @Author: JY
# @Date:   2019-01-24T10:29:08+09:00
# @Filename: generate_raw_data_for_ETRI_parsing_02.py
# @Last modified by:   JY
# @Last modified time: 2019-01-28T13:24:26+09:00
# @Copyright: JeeY

import time

sleeptime = 100000

file_path_00 = 'd:/Programming/Exercise_RNN/'
file_path_01 = 'd:/Programming/Corpus/'

read_file = '구문구조부착문장.sentence'
result_file_1 = 'result_raw_words_list_temp.words'

skip_sent_num = ['21742']

class sent_linked_list_node:
    def __init__(self, num):
        self.index_num = num
        self.parent_num = None
        self.word = None
        self.elements_of_word = list()
        self.next = None

full_words_list = list()
full_words_dict = dict()

def handle_one_sentence (f_r):
    up_sent_dict = dict()
    down_sent_dict = dict()
    sentence_0 = list()
    sentence_1 = list()
    w_switch = 1

    while True:
        line = f_r.readline()
        if 'Sentence No.' in line:
            for num in skip_sent_num:
                if num in line:
                    return None, None, None, None, None
            temp_sent_num = line
        if '-------' in line:
            break

    raw_sentence = f_r.readline()
    sentence_0 = raw_sentence.split()
    len_0 = len(sentence_0)
    f_r.readline()

    line_num_0 = 0
    while True:
        line = f_r.readline()
        if '------' in line:
            break
        line = line.split()

        up_sent_dict[line_num_0+1] = list()
        up_sent_dict[line_num_0+1].append(line[0])

        if len(line) == 1:
            while True:
                line = f_r.readline()
                if '======' in line:
                    return None, None, None, None, None
        if ']+' in line[1]:
            tmp_list = line[1].split(']+')

            for j in tmp_list:
                if j[-1] == ']':
                    if '[[' in j:
                        up_sent_dict[line_num_0+1].append([j[0], j[2:-1]])
                        # print(up_sent_dict[line[0]])
                        time.sleep(sleeptime)
                    else:
                        temp = j[:-1].split('[')
                        up_sent_dict[line_num_0+1].append([temp[0], temp[1]])
                else:
                    if '[[' in j:
                        up_sent_dict[line_num_0+1].append([j[0], j[2:]])
                    else:
                        temp = j.split('[')
                        up_sent_dict[line_num_0+1].append([temp[0], temp[1]])

        else:
            j = line[1]
            if j[-1] == ']':
                if '[[' in j:
                    up_sent_dict[line_num_0+1].append([j[0], j[2:-1]])
                    print(up_sent_dict[line[0]])
                    time.sleep(sleeptime)
                else:
                    temp = j[:-1].split('[')
                    up_sent_dict[line_num_0+1].append([temp[0], temp[1]])
            else:
                if '[[' in j:
                    up_sent_dict[line_num_0+1].append([j[0], j[2:]])
                else:
                    temp = j.split('[')
                    print(temp, line)
                    up_sent_dict[line_num_0+1].append([temp[0], temp[1]])
        line_num_0 += 1

    if len_0 != line_num_0:
        return None, None, None, None, None

    sentence_1 = f_r.readline().split()
    len_1 = len(sentence_1)
    f_r.readline()

    line_num_1 = 0
    while True:
        line = f_r.readline()
        if '======' in line:
            break
        line = line.split()
        down_sent_dict[line[0]] = list()
        down_sent_dict[line[0]].append(line[1])

        if ']+' in line[2]:
            tmp_list = line[2].split(']+')
            for j in tmp_list:
                if j[-1] == ']':
                    if '[[' in j:
                        down_sent_dict[line[0]].append([j[0], j[2:-1]])
                        print(down_sent_dict[line[0]])
                        time.sleep(sleeptime)
                    else:
                        temp = j[:-1].split('[')
                        down_sent_dict[line[0]].append([temp[0], temp[1]])
                else:
                    if '[[' in j:
                        down_sent_dict[line[0]].append([j[0], j[2:]])
                    else:
                        temp = j.split('[')
                        down_sent_dict[line[0]].append([temp[0], temp[1]])

        else:
            j = line[2]
            if j[-1] == ']':
                if '[[' in j:
                    down_sent_dict[line[0]].append([j[0], j[2:-1]])
                    print(down_sent_dict[line[0]])
                    time.sleep(sleeptime)
                else:
                    temp = j[:-1].split('[')
                    down_sent_dict[line[0]].append([temp[0], temp[1]])
            else:
                if '[[' in j:
                    down_sent_dict[line[0]].append([j[0], j[2:]])
                else:
                    temp = j.split('[')
                    down_sent_dict[line[0]].append([temp[0], temp[1]])

        line_num_1 += 1

    if len_1 != line_num_1:
        return None, None, None, None, None

    return up_sent_dict, down_sent_dict, sentence_0, sentence_1, raw_sentence

def make_up_sent_linked_list_node(up_dict, line_0):
    num = 1
    curr_node = sent_linked_list_node(num)
    for idnum in up_dict:
        if idnum == 1:
            head_node = curr_node
        curr_node.word = up_dict[idnum][0]
        for pl in up_dict[idnum][1:]:
            curr_node.elements_of_word.append(pl)

        num += 1
        before = curr_node
        curr_node.next = sent_linked_list_node(num)
        temp = curr_node.next
        curr_node = temp
    before.next = None
    now_node = head_node

    return head_node

def make_down_sent_linked_list_node(down_dict, line_1, up_dict):
    # print(up_dict)
    # print(down_dict)
    num = 1
    curr_node = sent_linked_list_node(num)
    for in_num in down_dict:
        # print(in_num)
        if num == 1:
            head_node = curr_node
        # print(down_dict[in_num])
        curr_node.index_num = in_num
        curr_node.parent_num = down_dict[in_num][0]

        for pl in down_dict[in_num][1:]:
            curr_node.elements_of_word.append(pl)

        num += 1
        before = curr_node
        curr_node.next = sent_linked_list_node(num)
        temp = curr_node.next
        curr_node = temp

    before.next = None
    # curr_node = None

    now_node = head_node
    # while True:
    #     print(now_node.index_num, ': ', now_node.parent_num)
    #     # print(now_node, now_node.next)
    #     if now_node.next is None:
    #         break
    #     new_node = now_node.next
    #     now_node = new_node
    return head_node

def make_full_words_list(up_head):
    curr_node = up_head
    while curr_node:
        for i in curr_node.elements_of_word:
            full_words_list.append(i)
        temp = curr_node.next
        curr_node = temp


filename_00 = './' + read_file

with open(filename_00, 'r', encoding='utf-8') as f1:
    # result_list_head = full_results_list_node()
    while True:
        line = f1.readline()
        if not line: break
        if '=====' in line:
            up_dict, down_dict, sen_0, sen_1, raw_sentence = handle_one_sentence(f1)

            if sen_0 != None:
                up_head = make_up_sent_linked_list_node(up_dict, sen_0)
                make_full_words_list(up_head)

with open(result_file_1, 'w', encoding='utf-8') as fw:

    for i in full_words_list:
        fw.write(str(i[0]) +'\t\t\t'+ str(i[1]) + '\n')









## end line
