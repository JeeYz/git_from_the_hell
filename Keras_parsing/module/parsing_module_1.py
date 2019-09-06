# @Author: J.Y.
# @Date:   2019-04-09T06:19:42+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-09-06T10:28:03+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import time
import numpy as np

fpath1 = 'd:/Program_Data/'
filename1 = fpath1 + 'raw_test_dataset_01.test'
filename3 = fpath1 + 'result_raw_words_list_00.words'
filename4 = fpath1 + 'result_pos_temp_01.pos'

def error_pause(comment, act_stack):
    print('error occured ', 'in ', comment, ' !!')
    print('\n')
    for i in act_stack:
        print('index : ', i.index)
        print('word : ', i.word)
        print('children : ', i.children)
        print('depend : ', i.depend)
        print('\n')
    time.sleep(10000)

def generate_temporary_data(test_words, word_data):
    # print(test_words)
    word = list()
    pos = list()
    for i in test_words:
        if i == 'NULL':
            word.append('NULL')
            pos.append('NULL')
            word.append('NULL')
            pos.append('NULL')
        elif i == 'ROOT':
            word.append('ROOT')
            pos.append('ROOT')
            word.append('ROOT')
            pos.append('ROOT')
        else:
            # print(word_data)
            for j in word_data:
                if i == j[2]:
                    word.append(j[3])
                    pos.append(j[4])
                    word.append(j[5])
                    pos.append(j[6])
    # print(len(word))
    # print(word)
    # print(len(pos))
    # print(pos)
    return word, pos

def generate_temporary_words_data(stack, buffer, act_stack):
    temp = list()
    if len(stack) < 3:
        for i in stack:
            temp.append(i)
        for j in range(3-len(stack)):
            temp.append('NULL')
    else:
        for i in range(3):
            temp.append(stack[i])
    if len(buffer) < 3:
        for i in buffer:
            temp.append(i)
        for j in range(3-len(buffer)):
            temp.append('NULL')
    else:
        for i in range(3):
            temp.append(buffer[i])
    if len(temp) != 6:
        error_pause('len(temp) != 6', act_stack)
    # print(temp, len(temp))
    for i in range(2):
        if stack[0] == 'ROOT':
            temp.extend(['NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL', 'NULL'])
            break
        if stack[1] == 'ROOT':
            temp.extend(['NULL', 'NULL', 'NULL', 'NULL'])
        else:
            for node in act_stack:
                if stack[i] == node.word:
                    if node.children == []:
                        temp.extend(['NULL', 'NULL', 'NULL', 'NULL'])
                    else:
                        if len(node.children) == 1:
                            temp.append(node.children[0])
                            temp.append(node.children[0])
                            temp.append('NULL')
                            temp.append('NULL')
                        else:
                            temp.append(node.children[0])
                            temp.append(node.children[-1])
                            temp.append(node.children[1])
                            temp.append(node.children[-2])
    # print(temp, len(temp))
    if len(temp) != 14:
        error_pause('len(temp) != 14', act_stack)
    for i in range(2):
        if stack[0] == 'ROOT':
            temp.extend(['NULL', 'NULL', 'NULL', 'NULL'])
            break
        elif stack[1] == 'ROOT':
            temp.extend(['NULL', 'NULL'])
        else:
            for node in act_stack:
                if stack[i] == node.word:
                    if node.children == []:
                        temp.extend(['NULL', 'NULL'])
                    else:
                        if len(node.children) == 1:
                            for m in act_stack:
                                if m.word == node.children[0]:
                                    if m.children == []:
                                        temp.extend(['NULL', 'NULL'])
                                    else:
                                        if len(m.children) == 1:
                                            temp.append(m.children[0])
                                            temp.append(m.children[0])
                                        else:
                                            temp.append(m.children[0])
                                            temp.append(m.children[-1])
                        else:
                            for m in act_stack:
                                if m.word == node.children[0]:
                                    if m.children == []:
                                        temp.extend(['NULL'])
                                    else:
                                        if len(m.children) == 1:
                                            temp.append(m.children[0])
                                        else:
                                            temp.append(m.children[0])
                                if m.word == node.children[-1]:
                                    if m.children == []:
                                        temp.extend(['NULL'])
                                    else:
                                        if len(m.children) == 1:
                                            temp.append(m.children[-1])
                                        else:
                                            temp.append(m.children[-1])
    # print(temp, len(temp))
    if len(temp) != 18:
        error_pause('len(temp) != 18', act_stack)
    return temp

def generate_data_of_test(action, stack, buffer, w_dict, p_dict, word_data, act_stack):
    data = list()

    if action == 'shift' and buffer == []:
        return data, 0, stack, buffer, act_stack

    if action == 'shift':
        stack.insert(0, buffer[0])
        del buffer[0]
        temp = generate_temporary_words_data(stack, buffer, act_stack)
        word, pos = generate_temporary_data(temp, word_data)
        #### return

    elif action == 'left':
        if len(stack) > 2:
            for index, node in enumerate(act_stack):
                if stack[0] == node.word:
                    node.children.append(stack[1])
                if stack[1] == node.word:
                    node.depend = stack[0]
            del stack[1]
            temp = generate_temporary_words_data(stack, buffer, act_stack)
            word, pos = generate_temporary_data(temp, word_data)
            #### return
        else:
            return data, 0, stack, buffer, act_stack

    elif action == 'right':
        if len(stack) >= 2:
            for index, node in enumerate(act_stack):
                if stack[1] == node.word:
                    node.children.append(stack[0])
                if stack[0] == node.word:
                    node.depend = stack[1]
            del stack[0]
            temp = generate_temporary_words_data(stack, buffer, act_stack)
            word, pos = generate_temporary_data(temp, word_data)
            #### return
        else:
            return data, 0, stack, buffer, act_stack

    else:
        error_pause('action == wrong')

    data.append(word)
    data.append(pos)
    data = change_to_number(w_dict, p_dict, word_data, data)

    return data, 1, stack, buffer, act_stack

def change_to_number(w_dict, p_dict, word_data, data):
    new_word = list()
    new_pos = list()

    for i,j in enumerate(data[0]):
        new_word.append(w_dict[j])
        new_pos.append(p_dict[data[1][i]])

    del data
    data = list()
    data.append([new_word])
    data.append([new_pos])

    return data

def make_parsing_table(action_stack):
    result = list()
    for i,j in enumerate(action_stack, 1):
        one_word = list()
        one_word.append(int(i))
        if str(j.depend) == 'None':
            one_word.append(int(0))
        else:
            t = str(j.depend)
            t = t.split("__")
            # print(t)
            if t[0] == 'ROOT':
                one_word.append(0)
            else:
                one_word.append(t[1])
        result.append(one_word)
    if len(action_stack) != len(result):
        error_pause('action == result', action_stack)
    return result

def evaluate_result(table, word_data):
    c = 0
    for i,j in enumerate(word_data):
        if int(table[i][1]) == int(j[1]):
            c += 1
    q = len(word_data)
    return c, q










if __name__ == '__main__':
    print('hello, world~!~!')

## endl
