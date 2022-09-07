# @Author: JY
# @Date:   2019-01-15T16:22:38+09:00
# @Filename: generate_raw_data_for_ETRI_parsing_01.py
# @Last modified by:   JY
# @Last modified time: 2019-01-24T10:39:57+09:00
# @Copyright: JeeY


file_path_00 = 'd:/Programming/Exercise_RNN/'
file_path_01 = 'd:/Programming/Corpus/'

read_file = '구문구조부착문장.sentence'
result_file = 'result_01.result'

skip_sent_num = ['21742']

class up_sent_linked_list_node:
    def __init__(self, num):
        self.index_num = num
        self.parent_num = None
        self.word = None
        self.elements_of_word = dict()
        self.next = None

class down_sent_linked_list_node:
    def __init__(self, num):
        self.index_num = num
        self.parent_num = None
        self.word = None
        self.elements_of_word = dict()
        self.next = None

class result_sent_linked_list_node:
    def __init__(self):
        self.word = None
        self.index_num = None
        self.parent_num = None
        self.elements_of_word = dict()
        self.next = None

class full_results_list_node:
    def __init__(self):
        # self.head = None
        self.index_num = None
        self.sentence = None
        self.each_list_address = None
        self.next = None

result_full_list = full_results_list_node()
result_full_list_head = full_results_list_node()
result_full_list = result_full_list_head
# result_full_list.head = result_full_list_head

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
                    return None, None, None, None
            temp_sent_num = line
        if '-------' in line:
            break

    sentence_0 = f_r.readline().split()
    len_0 = len(sentence_0)
    f_r.readline()

    line_num_0 = 0
    while True:
        line = f_r.readline()
        if '------' in line:
            break
        line = line.split()
        up_sent_dict[line[0]] = list()

        if len(line) == 1:
            while True:
                line = f_r.readline()
                if '======' in line:
                    return None, None, None, None
        if ']+' in line[1]:
            tmp_list = line[1].split(']+')
            for j in tmp_list:
                up_sent_dict[line[0]].append(j)
        else:
            up_sent_dict[line[0]].append(line[1])
        line_num_0 += 1

    if len_0 != line_num_0:
        return None, None, None, None

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
                down_sent_dict[line[0]].append(j)
        else:
            down_sent_dict[line[0]].append(line[2])
        line_num_1 += 1

    if len_1 != line_num_1:
        return None, None, None, None

    return up_sent_dict, down_sent_dict, sentence_0, sentence_1

def make_up_sent_linked_list_node(up_sent, line_0):
    # up_sent is dictionary
    # line_0 is string of sentence
    head = up_sent_linked_list_node(1)
    num = 0
    for word in up_sent:
        num += 1
        if num == 1:
            curr_node = head
            curr_node.word = word

            for i in range(len(up_sent[word])):
                if '[[' in up_sent[word][i]:
                    tmp = list()
                    tmp.append(up_sent[word][i][0])
                    tmp.append(up_sent[word][i][2:])
                else:
                    tmp = up_sent[word][i].split('[')

                if tmp[1][-1] == ']':
                    tmp[1] = tmp[1][:-1]
                curr_node.elements_of_word[i] = [tmp[0], tmp[1]]

        else:
            curr_node.next = up_sent_linked_list_node(num)
            temp_node = curr_node.next
            curr_node = temp_node
            curr_node.word = word
            for i in range(len(up_sent[word])):
                if '[[' in up_sent[word][i]:
                    tmp = list()
                    tmp.append(up_sent[word][i][0])
                    tmp.append(up_sent[word][i][2:])
                else:
                    tmp = up_sent[word][i].split('[')

                if tmp[1][-1] == ']':
                    tmp[1] = tmp[1][:-1]
                curr_node.elements_of_word[i] = [tmp[0], tmp[1]]

    now_node = head
    # while True:
    #     print(now_node.index_num, ': ', now_node.word)
    #     # print(now_node, now_node.next)
    #     if now_node.next is None:
    #         break
    #     new_node = now_node.next
    #     now_node = new_node
    return head

def make_down_sent_linked_list_node(down_sent, line_1, up_sent):
    # down_sent is dictionary
    # line_1 is string of sentence
    # up_sent is dictionary
    # print(down_sent)
    head = down_sent_linked_list_node(1)
    num = 0
    for word in down_sent:
        # print(word)
        num += 1
        if num == 1:
            curr_node = head
            curr_node.word = word
            curr_node.parent_num = down_sent[word][0]

            for i in range(len(down_sent[word][1:])):
                if '[[' in down_sent[word][i+1]:
                    tmp = list()
                    tmp.append(down_sent[word][i+1][0])
                    tmp.append(down_sent[word][i+1][2:])
                else:
                    tmp = down_sent[word][i+1].split('[')

                if tmp[1][-1] == ']':
                    tmp[1] = tmp[1][:-1]
                curr_node.elements_of_word[i] = [tmp[0], tmp[1]]

        else:
            curr_node.next = down_sent_linked_list_node(num)
            temp_node = curr_node.next
            curr_node = temp_node
            curr_node.word = word
            curr_node.parent_num = down_sent[word][0]

            for i in range(len(down_sent[word][1:])):
                if '[[' in down_sent[word][i+1]:
                    tmp = list()
                    tmp.append(down_sent[word][i+1][0])
                    tmp.append(down_sent[word][i+1][2:])
                else:
                    tmp = down_sent[word][i+1].split('[')

                if tmp[1][-1] == ']':
                    tmp[1] = tmp[1][:-1]
                curr_node.elements_of_word[i] = [tmp[0], tmp[1]]

    now_node = head

    # while True:
    #     print(now_node.index_num, ': ', now_node.parent_num)
    #     # print(now_node, now_node.next)
    #     if now_node.next is None:
    #         break
    #     new_node = now_node.next
    #     now_node = new_node
    return head

def check_being_or_not_in_down_LL(down_head, target_word):
    curr_node = down_head
    while True:
        # print(curr_node.elements_of_word)
        # print(curr_node)
        if str(target_word) == str(curr_node.elements_of_word[0][0]):
            return 1

        temp_node = curr_node.next
        curr_node = temp_node
        if curr_node is None:
            # print(target_word)
            return 0

def check_chunking(up_head, down_head, sen_0):
    # print(sen_0)
    length0 = len(sen_0)
    # print('======================= : ', length0)
    up_curr_node = up_head
    down_curr_node = down_head
    before_ret_num = None
    for i in range(length0):
        after_node = up_curr_node.next
        if after_node == None: break

        target_word = after_node.elements_of_word[0][0]
        result = check_being_or_not_in_down_LL(down_head, target_word)

        if int(result) == 1 and before_ret_num == 0:
            # print('++', result, ' : ', target_word)
            up_curr_node.parent_num = after_node.index_num
            before_ret_num = result
            # print('++', target_word, ' : ', up_curr_node.parent_num, up_curr_node.word, up_curr_node.index_num)
        elif int(result) == 0:
            # print('++', result, ' : ', target_word)
            up_curr_node.parent_num = after_node.index_num
            before_ret_num = result
            # print('++', target_word, ' : ', up_curr_node.parent_num, up_curr_node.word, up_curr_node.index_num)
        else:
            before_ret_num = result
        temp_node = up_curr_node.next
        up_curr_node = temp_node
        # if after_node is None: break


def look_up_word_in_up_LL(target_word, up_head):
    curr_node = up_head
    while True:
        if curr_node == None: break
        if str(target_word) == str(curr_node.elements_of_word[0][0]):
            return curr_node.index_num
        temp_node = curr_node.next
        curr_node = temp_node

def check_pos_positive(down_head, target_num):
    curr_node = down_head
    while True:
        # print('before if : ', target_num, curr_node.index_num)
        if curr_node == None: break
        if int(target_num) == int(curr_node.index_num):
            # print('after if : ', target_num, curr_node.index_num)
            if curr_node.elements_of_word[0][1] == '긍정지정사':
                return  curr_node.parent_num
            else:
                return None
        temp_node = curr_node.next
        curr_node = temp_node

def look_up_word_in_down_linked_list(target_word, up_head, down_head):

    curr_node = down_head
    while True:
        # print('\t=====\thello, world\t=====')
        # print(target_word, curr_node.elements_of_word)
        # print('\n\t=====', curr_node, '=====\t')

        if curr_node == None: break
        if str(target_word) == str(curr_node.elements_of_word[0][0]):
            target_num = int(curr_node.parent_num)
            if target_num == 0:
                result = None
            else:
                result = check_pos_positive(down_head, target_num)

            if result != None:
                return_word = look_up_parent_num_in_down_linked_list(result, down_head)
                return look_up_word_in_up_LL(return_word, up_head)
            else:
                # print('\t\t\t\thello, world~!~!')
                return_word = curr_node.elements_of_word[0][0]
                return look_up_word_in_up_LL(return_word, up_head)

        # print('\t=====\thello, world\t=====')
        # print(target_word, curr_node.elements_of_word)
        temp_node = curr_node.next
        curr_node = temp_node

def look_up_parent_num_in_down_linked_list(target_pnum, down_head):
    curr_node = down_head
    while True:
        if curr_node == None:break
        if target_pnum == curr_node.index_num:
            return curr_node.elements_of_word[0][0]

        temp_node = curr_node.next
        curr_node = temp_node

def make_full_list(sen_0, up_head, down_head, num, sent_num):
    global result_full_list
    global result_full_list_head

    if num == 1:
        global result_head
        result_head = result_sent_linked_list_node()
        curr_node = result_head
        up_curr_node = up_head

        check_chunking(up_head, down_head, sen_0)

        while up_curr_node:
            curr_node.index_num = up_curr_node.index_num
            curr_node.word = up_curr_node.word
            curr_node.elements_of_word = up_curr_node.elements_of_word

            if up_curr_node.parent_num == None:
                # print('+++++++', up_curr_node.elements_of_word)
                search_word = up_curr_node.elements_of_word[0][0]
                # print('=== : ', up_curr_node.elements_of_word, up_curr_node.parent_num)
                ret_parent_num = look_up_word_in_down_linked_list(search_word, up_head, down_head)
                curr_node.parent_num = ret_parent_num
            else:
                curr_node.parent_num = up_curr_node.parent_num

            temp_node = up_curr_node.next
            up_curr_node = temp_node

            curr_node.next = result_sent_linked_list_node()
            temp_node = curr_node.next
            curr_node = temp_node

    else:
        curr_node = result_sent_linked_list_node()
        result_head = curr_node

        up_curr_node = up_head
        # print('\t\t\thello, world~!~!')
        check_chunking(up_head, down_head, sen_0)

        while up_curr_node:
            curr_node.index_num = up_curr_node.index_num
            curr_node.word = up_curr_node.word
            curr_node.elements_of_word = up_curr_node.elements_of_word

            if up_curr_node.parent_num == None:
                search_word = up_curr_node.elements_of_word[0][0]
                ret_parent_num = look_up_word_in_down_linked_list(search_word, up_head, down_head)
                curr_node.parent_num = ret_parent_num
            else:
                curr_node.parent_num = up_curr_node.parent_num

            temp_node = up_curr_node.next
            up_curr_node = temp_node

            curr_node.next = result_sent_linked_list_node()
            temp_node = curr_node.next
            curr_node = temp_node

    result_full_list.index_num = sent_num
    # print('+ + + + + result_head type : ', type(result_head))
    result_full_list.each_list_address = result_head
    # print('= = = = = each list addr type : ', type(result_full_list.each_list_address))
    result_full_list.next = full_results_list_node()
    temp_node = result_full_list.next
    result_full_list = temp_node
    # print('++++++++++++++++++++\t hello, world~! \t++++++++++++++++++++')


filename_00 = './' + read_file

with open(filename_00, 'r', encoding='utf-8') as f1:
    result_list_head = full_results_list_node()
    num = 0
    sent_num = 0
    while True:
        line = f1.readline()
        if not line: break
        if '=====' in line:
            up_dict, down_dict, sen_0, sen_1 = handle_one_sentence(f1)

            if sen_0 is not None:
                # print(sen_0)
                up_head = make_up_sent_linked_list_node(up_dict, sen_0)
                down_head = make_down_sent_linked_list_node(down_dict, sen_1, up_dict)
                # print(up_head.elements_of_word, down_head.elements_of_word)
                result_list_head = make_full_list(sen_0, up_head, down_head, num+1, sent_num+1)
                num += 1
                sent_num += 1


## print session
# now_node  = result_full_list_head
# while True:
#     if now_node == None: break
#     print(now_node.index_num)
#     print(type(now_node))
#     curr_node = now_node.each_list_address
#     print(type(now_node.each_list_address), type(curr_node))
#     while True:
#         if curr_node == None: break
#         print(type(curr_node))
#         print('++ : ', curr_node.index_num, ' --- ', curr_node.parent_num)
#         temp_node = curr_node.next
#         curr_node = temp_node
#     print('==================================================================\n\n')
#     temp_node = now_node.next
#     now_node = temp_node


## generate file Session

now_node  = result_full_list_head
with open(result_file, 'w', encoding='utf-8') as fw:
    while True:
        if now_node == None: break
        curr_node = now_node.each_list_address
        fw.write('No.' + str(now_node.index_num) + '\n')
        while True:
            if curr_node == None: break

            fw.write(str(curr_node.index_num) + '\t\t' + str(curr_node.word) + '\t\t')
            fw.write(str(curr_node.parent_num) + '\t' + str(curr_node.elements_of_word) + '\n')

            temp_node = curr_node.next
            curr_node = temp_node
        temp_node = now_node.next
        now_node = temp_node
        fw.write('\n\n\n')
        print('one sentence complete!!\t', now_node.index_num)



















## end line
