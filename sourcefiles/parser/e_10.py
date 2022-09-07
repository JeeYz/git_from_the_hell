# @Author: JY
# @Date:   2019-01-29T14:00:58+09:00
# @Filename: e_10.py
# @Last modified by:   JY
# @Last modified time: 2019-01-29T14:24:55+09:00
# @Copyright: JeeY



import time

sleeptime = 360000

file_path_00 = 'd:/Programming/Exercise_RNN/'
file_path_01 = 'd:/Programming/Corpus/'

read_file = '구문구조부착문장.sentence'
result_file = 'result_02.result'

skip_sent_num = ['21742']

class sent_linked_list_node:
    def __init__(self, num):
        self.index_num = num
        self.parent_num = None
        self.word = None
        self.elements_of_word = list()
        self.next = None

class full_results_list_node:
    def __init__(self):
        self.index_num = None
        self.sentence = None
        self.result_dict = dict()
        self.next = None

result_full_list = full_results_list_node()
result_full_list_head = full_results_list_node()
result_full_list = result_full_list_head

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
        # print('++ : ', line)
        # print('== : ', line[0])
        # print(up_sent_dict, '\n\n')
        up_sent_dict[line_num_0+1] = list()
        up_sent_dict[line_num_0+1].append(line[0])
        # print(up_sent_dict)
        if len(line) == 1:
            while True:
                line = f_r.readline()
                if '======' in line:
                    return None, None, None, None, None
        if ']+' in line[1]:
            # print(line[1])
            tmp_list = line[1].split(']+')
            # print(tmp_list)
            for j in tmp_list:
                # print(line)
                # time.sleep(sleeptime)
                if j[-1] == ']':
                    if '[[' in j:
                        up_sent_dict[line_num_0+1].append([j[0], j[2:-1]])
                        # print(up_sent_dict[line[0]])
                        time.sleep(sleeptime)
                    else:
                        temp = j[:-1].split('[')
                        # print(temp)
                        up_sent_dict[line_num_0+1].append([temp[0], temp[1]])
                        # print('******* : ', line[0])
                else:
                    if '[[' in j:
                        up_sent_dict[line_num_0+1].append([j[0], j[2:]])
                    else:
                        temp = j.split('[')
                        # print(temp)
                        up_sent_dict[line_num_0+1].append([temp[0], temp[1]])

            # print('\n')
            # print(up_sent_dict)
            # print('\n')
            # time.sleep(sleeptime)

        else:
            # print(line)
            # time.sleep(sleeptime)
            j = line[1]
            if j[-1] == ']':
                if '[[' in j:
                    up_sent_dict[line_num_0+1].append([j[0], j[2:-1]])
                    print(up_sent_dict[line[0]])
                    time.sleep(sleeptime)
                else:
                    temp = j[:-1].split('[')
                    # print(temp)
                    up_sent_dict[line_num_0+1].append([temp[0], temp[1]])
            else:
                if '[[' in j:
                    up_sent_dict[line_num_0+1].append([j[0], j[2:]])
                else:
                    temp = j.split('[')
                    print(temp, line)
                    up_sent_dict[line_num_0+1].append([temp[0], temp[1]])
        # print('* * * * *\n')
        # print(up_sent_dict)
        # print('\n')
        line_num_0 += 1

    if len_0 != line_num_0:
        # print(sentence_0)
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
        # print(line)
        # time.sleep(sleeptime)

        if ']+' in line[2]:
            tmp_list = line[2].split(']+')
            # print(tmp_list)
            for j in tmp_list:
                if j[-1] == ']':
                    if '[[' in j:
                        down_sent_dict[line[0]].append([j[0], j[2:-1]])
                        print(down_sent_dict[line[0]])
                        time.sleep(sleeptime)
                    else:
                        temp = j[:-1].split('[')
                        # print(temp)
                        down_sent_dict[line[0]].append([temp[0], temp[1]])
                else:
                    if '[[' in j:
                        down_sent_dict[line[0]].append([j[0], j[2:]])
                    else:
                        temp = j.split('[')
                        # print(temp)
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
                    # print(temp)
                    down_sent_dict[line[0]].append([temp[0], temp[1]])
            else:
                if '[[' in j:
                    down_sent_dict[line[0]].append([j[0], j[2:]])
                else:
                    temp = j.split('[')
                    # print(temp)
                    down_sent_dict[line[0]].append([temp[0], temp[1]])

        line_num_1 += 1

    if len_1 != line_num_1:
        return None, None, None, None, None

    return up_sent_dict, down_sent_dict, sentence_0, sentence_1, raw_sentence

def make_up_sent_linked_list_node(up_dict, line_0):
    # print(up_dict)
    # print(len(up_dict))
    num = 1
    curr_node = sent_linked_list_node(num)
    for idnum in up_dict:
        if idnum == 1:
            head_node = curr_node
        # print(up_dict[idnum][0])
        curr_node.word = up_dict[idnum][0]
        # print(up_dict[idnum][1:])
        for pl in up_dict[idnum][1:]:
            curr_node.elements_of_word.append(pl)

        num += 1
        before = curr_node
        curr_node.next = sent_linked_list_node(num)
        temp = curr_node.next
        curr_node = temp
    # print(num)
    # print(curr_node)
    before.next = None
    # curr_node = None
    # print(curr_node)
    now_node = head_node

    # while True:
    #     print(now_node.index_num, ': ', now_node)
    #     print(now_node.word, now_node.elements_of_word)
    #     # print(now_node, now_node.next)
    #     if now_node.next is None:
    #         break
    #     new_node = now_node.next
    #     now_node = new_node
    # curr_node = None
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


filename_00 = './' + read_file

result_list = list()

with open(filename_00, 'r', encoding='utf-8') as f1:
    result_list_head = full_results_list_node()
    num = 0
    while True:
        line = f1.readline()
        if not line: break
        if '=====' in line:
            up_dict, down_dict, sen_0, sen_1, raw_sentence = handle_one_sentence(f1)
            # print(sen_0)
            # print(sen_1)
            # print(up_dict)
            # print(down_dict)
            # print('\n\n\n\n\n')

            result_list.append(down_dict)

            # for i in down_dict:
            #     print(i, down_dict[i][0], down_dict[i])
            #     if int(i) >= int(down_dict[i][0]) and int(down_dict[i][0]) != 0:
            #         print('** hello, world **')

for i in result_list:
    for j in down_dict:
        # print(j, down_dict[j][0], down_dict[j])
        if int(j) >= int(down_dict[j][0]) and int(down_dict[j][0]) != 0:
            print('** hello, world **')










## end line
