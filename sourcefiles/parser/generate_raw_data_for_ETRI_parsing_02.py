# @Author: JY
# @Date:   2019-01-24T10:29:08+09:00
# @Filename: generate_raw_data_for_ETRI_parsing_02.py
# @Last modified by:   JeeY
# @Last modified time: 2019-02-01T00:34:12+09:00
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

def check_being_or_not_in_down_LL(down_head, target_word, raw_sentence, info):
    # info = [word, index, th, freq]
    if int(info[3]) == 1:
        curr_node = down_head
        while curr_node:
            temp = list()
            temppara = 0
            for i in curr_node.elements_of_word:
                for j in i[0].split('_'):
                    temp.append(j)
            if str(target_word) in temp:
                # print(curr_node.elements_of_word[0][0], '\t', target_word, '\t', curr_node.parent_num)
                return 1, curr_node.parent_num
            temp_node = curr_node.next
            curr_node = temp_node
        return 0, None
    else:
        num = 1
        curr_node = down_head
        while curr_node:
            temp = list()
            temppara = 0
            for i in curr_node.elements_of_word:
                for j in i[0].split('_'):
                    temp.append(j)

            if str(target_word) in temp\
            and int(info[2]) == num:
                # print(curr_node.elements_of_word[0][0], '\t', target_word, '\t', curr_node.parent_num)
                return 1, curr_node.parent_num
            elif str(target_word) in temp\
            and int(info[2]) != num:
                num += 1
            temp_node = curr_node.next
            curr_node = temp_node
        return 0, None

def return_word_from_down_LL(result, down_head):
    curr_node = down_head
    while curr_node:
        # print(result, curr_node.elements_of_word)
        if int(result) == int(curr_node.index_num):
            # print(result, curr_node.elements_of_word)
            if curr_node.elements_of_word[0][1] == '긍정지정사':
                return_word = return_word_from_down_LL(int(result)-1, down_head)
            else:
                return_word = curr_node.elements_of_word[0][0].split('_')[0]
                # print('%% : ', curr_node.elements_of_word, return_word)
            return return_word
        temp_node = curr_node.next
        curr_node = temp_node
    # print('++ not in down linked list ++')
    # time.sleep(sleeptime)

def generate_word_info(word, word_list, index):
    # print(word_list)
    word_info = list()
    n1, n2 = 0, 0
    for i, j in enumerate(word_list):
        for k in j:
            if str(word) == str(k):
                # print('hello, world')
                n2 += 1
            # print(index, word_list, word)
        if int(index) == (i+1):
            n1 = n2
    if word == "'" or word == '"':
        n1 = int(n1/2)
        n2 = int(n2/2)
    word_info.append(word)
    word_info.append(index)
    word_info.append(n1)
    word_info.append(n2)
    return word_info

def check_chunking(up_head, down_head, sen_0, raw_sentence, up_word_list, down_word_list):
    temp_list_freq = list()
    length = len(sen_0)
    curr_node = up_head
    fixed_pnum = int()
    curr = curr_node
    # while curr:
    #     print(curr.elements_of_word)
    #     temp = curr.next
    #     curr = temp

    for i in range(length-1):
        next_node = curr_node.next
        # print(i, ' : ', length, next_node.elements_of_word)
        target_word = curr_node.elements_of_word[0][0].split('_')[0]
        info0 = generate_word_info(target_word, up_word_list, i+1)
        # print('+ : ', target_word)
        result0, pnum0 = check_being_or_not_in_down_LL(down_head, target_word, raw_sentence, info0)
        # if target_word == "'":
        #     print('++ : ', target_word, info0, result0, pnum0)

        if pnum0 != None:
            word0 = return_word_from_down_LL(pnum0, down_head)
            info_p0 = generate_word_info(word0, down_word_list, pnum0)
            # print(up_word_list)
            # print(word0, info_p0)
            pnum0 =look_up_word_in_up_LL(word0, up_head, info_p0)
            # print(pnum0)

        target_word = next_node.elements_of_word[0][0].split('_')[0]
        info1 = generate_word_info(target_word, up_word_list, i+2)
        # print('= : ', target_word, info1)
        result1, pnum1 = check_being_or_not_in_down_LL(down_head, target_word, raw_sentence, info1)
        # if target_word == "'":
        #     print('** : ', target_word, info1, result0, result1, pnum1)
        # print('== : ', result0, result1, '\t', fixed_pnum, pnum0, pnum1)
        if pnum1 != None:
            word1 = return_word_from_down_LL(pnum1, down_head)
            info_p1 = generate_word_info(word1, down_word_list, i+2)
            pnum1 =look_up_word_in_up_LL(word1, up_head, info_p1)

        if int(result0) == 1 and int(result1) == 0:
            # print(curr_node.elements_of_word, '\t', result0, result1)
            curr_node.parent_num = next_node.index_num
            # print('++ : ', pnum0, target_word)
            fixed_pnum = pnum0
        elif int(result0) == 0 and int(result1) == 1:
            # print(curr_node.elements_of_word, '\t', result0, result1)
            # print('== : ', fixed_pnum, target_word)
            curr_node.parent_num = fixed_pnum
            # print(curr_node.elements_of_word, curr_node.parent_num)
            fixed_pnum = int()
        elif int(result0) == 0 and int(result1) == 0:
            # print(curr_node.elements_of_word, '\t', result0, result1)
            curr_node.parent_num = next_node.index_num

        temp_node = curr_node.next
        curr_node = temp_node
    curr_node.parent_num = 0

def look_up_word_in_up_LL(target_word, up_head, info):
    ## info = [word, index, th, freq]
    curr_node = up_head
    num = 1
    # print(info)
    while curr_node:
        # print(target_word, curr_node.elements_of_word)
        temp = list()
        for i in curr_node.elements_of_word:
            for j in i[0].split('_'):
                temp.append(j)
        if str(target_word) in temp\
        and info[2] == num:
            # print(target_word, curr_node.elements_of_word)
            # print(target_word)
            # print('4. ', curr_node.elements_of_word, curr_node.parent_num, curr_node.index_num)
            if str(curr_node.elements_of_word[0][1]) == '긍정지정사':
                print(target_word, info, curr_node.elements_of_word)
                return int(curr_node.index_num)-1
            else:
                # print(curr_node.index_num)
                return curr_node.index_num
        if str(target_word) in temp\
        and info[2] != num:
            num += 1
        temp_node = curr_node.next
        curr_node = temp_node
    # print(target_word)
    # print('** not in down up list **')
    # time.sleep(sleeptime)

def check_pos_positive(down_head, target_num):
    curr_node = down_head
    while curr_node.next:
        # print('before if : ', target_num, curr_node.index_num)
        if int(target_num) == int(curr_node.index_num):
            # print('after if : ', target_num, curr_node.index_num)
            if curr_node.next.elements_of_word[0][1] == '긍정지정사':
                # print('1. ', curr_node.elements_of_word, curr_node.parent_num)
                # print('2. ', curr_node.next.elements_of_word, curr_node.next.parent_num)
                # time.sleep(sleeptime)
                return  curr_node.next.parent_num
            else:
                return curr_node.parent_num
        temp_node = curr_node.next
        curr_node = temp_node

def look_up_word_in_down_linked_list(target_word, up_head, down_head, info, up_word_list, down_word_list):
    ## info = [word, index, th, freq]
    curr_node = down_head
    num = 1
    # print(info)
    while curr_node:
        temp = list()
        for i in curr_node.elements_of_word:
            for j in i[0].split('_'):
                temp.append(j)
        # print(target_word, temp)
        # print(info[2], num)
        if str(target_word) in temp\
        and info[2] == num:
            # print(num)
            target_num = int(curr_node.index_num)
            if target_num == 0:
                return 0
            else:
                # print('\t * :', target_num)
                result = check_pos_positive(down_head, target_num)
                # print(result)

            return_word = look_up_parent_num_in_down_linked_list(result, down_head)

            if return_word != None:
                # print(return_word)
                r_info = generate_word_info(return_word, down_word_list, result)
            else:
                r_info = [None, None, None, None]

            return look_up_word_in_up_LL(return_word, up_head, r_info)
        if str(target_word) in temp\
        and info[2] != num:
            num += 1
            # print('hello, world', num)
        temp_node = curr_node.next
        curr_node = temp_node

def look_up_parent_num_in_down_linked_list(target_pnum, down_head):
    curr_node = down_head
    while curr_node:
        if target_pnum == curr_node.index_num:
            if curr_node.elements_of_word[0][1] == '긍정지정사':
                # print('5. ', curr_node.elements_of_word, curr_node.parent_num)
                # print('6. ', before.elements_of_word, before.parent_num)
                return before.elements_of_word[0][0].split('_')[0]
            else:
                # print('3. ', curr_node.elements_of_word, curr_node.parent_num)
                return curr_node.elements_of_word[0][0].split('_')[0]

        before = curr_node
        temp_node = curr_node.next
        curr_node = temp_node


def make_full_list(sen_0, up_head, down_head, num, raw_sentence,
                   up_word_list, down_word_list):

    global result_full_list
    global result_full_list_head
    global result_head

    curr_node = result_full_list_head

    while True:
        if curr_node.next == None: break
        temp_node = curr_node.next
        curr_node = temp_node

    curr_node.index_num = num
    curr_node.sentence = sen_0 # sen_0 is list
    curr_node.next = full_results_list_node()

    up_curr_node = up_head

    check_chunking(up_head, down_head, sen_0, raw_sentence,
                   up_word_list, down_word_list)
    curr = up_curr_node
    while curr:
        # print(curr.elements_of_word)
        # print(curr.parent_num)
        temp = curr.next
        curr = temp

    while up_curr_node:
        word_num = up_curr_node.index_num
        curr_node.result_dict[word_num] = list()

        if up_curr_node.parent_num == None:
            search_word = up_curr_node.elements_of_word[0][0]
            # print('+ :', search_word, up_curr_node.parent_num)
            info = generate_word_info(search_word, up_word_list, up_curr_node.index_num)
            # print(info)
            ret_parent_num = look_up_word_in_down_linked_list(search_word, up_head,
                                                              down_head, info, up_word_list, down_word_list)
            # print(ret_parent_num)
            curr_node.result_dict[word_num].append(ret_parent_num)
        else:
            curr_node.result_dict[word_num].append(up_curr_node.parent_num)

        curr_node.result_dict[word_num].append(up_curr_node.word)

        for word in up_curr_node.elements_of_word:
            # print(word)
            curr_node.result_dict[word_num].append(word)

        temp_node = up_curr_node.next
        up_curr_node = temp_node

    # print('++++++++++++++++++++\t hello, world~! \t++++++++++++++++++++')


filename_00 = './' + read_file

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

            if sen_0 != None:
                up_word_list = list()
                down_word_list = list()
                up_head = make_up_sent_linked_list_node(up_dict, sen_0)
                down_head = make_down_sent_linked_list_node(down_dict, sen_1, up_dict)
                ## make list
                curr = up_head
                while curr:
                    # print(curr.elements_of_word)
                    a = list()
                    for i in curr.elements_of_word:
                        for j in i[0].split('_'):
                            a.append(j)
                    up_word_list.append(a)
                    temp = curr.next
                    curr = temp
                curr = down_head
                while curr:
                    a = list()
                    for i in curr.elements_of_word:
                        for j in i[0].split('_'):
                            a.append(j)
                    down_word_list.append(a)
                    temp = curr.next
                    curr = temp
                # print(down_word_list)
                # print(up_word_list, down_word_list)
                ## end making list
                result_list_head = make_full_list(sen_0, up_head, down_head,
                                                  num+1, raw_sentence,
                                                  up_word_list, down_word_list)
                # time.sleep(sleeptime)
                # print('\n\n')
                # if num == 40:
                #     time.sleep(sleeptime)
                if num%1000 == 0:
                    print(num, ' of line complete!!')
                num += 1

curr_node  = result_full_list_head
with open(result_file, 'w', encoding='utf-8') as fw:
    while curr_node:
        # if now_node == None: break
        fw.write('No.' + str(curr_node.index_num) + '\n')

        fw.write(str(curr_node.sentence) + '\n')
        for i in curr_node.result_dict:
            fw.write(str(i) +'\t\t'+ str(curr_node.result_dict[i][0]) +'\t\t')
            fw.write(str(curr_node.result_dict[i][1]) +'\t\t')
            for j in curr_node.result_dict[i][2:]:
                for k in j:
                    fw.write(str(k))
                    fw.write('\t\t')
            fw.write('\n')

        fw.write('\n\n\n')
        print('one sentence complete!!\t', curr_node.index_num)
        temp_node = curr_node.next
        curr_node = temp_node









## end line
