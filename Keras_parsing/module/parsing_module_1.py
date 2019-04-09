# @Author: J.Y.
# @Date:   2019-04-09T06:19:42+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-09T12:33:58+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import time

fpath1 = 'd:/Program_Data/'
filename1 = fpath1 + 'raw_test_dataset_01.test'
filename3 = fpath1 + 'result_raw_words_list_00.words'
filename4 = fpath1 + 'result_pos_temp_01.pos'

def error_pause(comment):
    print('error occured ', 'in ', comment, ' !!')
    time.sleep(10000)

def generate_data_of_test(action, stack, buffer, w_dict, p_dict, words, act_stack):
    data = list()
    if action == 'shift':
        stack.insert(0, buffer[0])
        del buffer[0]
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
            error_pause('len(temp) != 6')
        for i in range(2):
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
        if len(temp) != 14:
            error_pause('len(temp) != 14')
        for i in range(2):
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
                                            
    elif action == 'left':
        if len(stack) > 2:
            for index, node in enumerate(act_stack):
                if stack[0] == node.word:
                    node.children.append(stack[1])
                if stack[1] == node.word:
                    node.depend = stack[0]
            temp = list()
    elif action == 'right':
        if len(stack) > 2:
            for index, node in enumerate(act_stack):
                if stack[1] == node.word:
                    node.children.append(stack[0])
                if stack[0] == node.word:
                    node.depend = stack[1]
            temp = list()
    else:
        error_pause('action == wrong')
    return data






if __name__ == '__main__':
    print('hello, world~!~!')

## endl
