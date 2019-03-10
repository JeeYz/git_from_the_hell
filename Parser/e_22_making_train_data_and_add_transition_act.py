# @Author: JY
# @Date:   2019-02-13T10:45:05+09:00
# @Filename: e_22.py
# @Last modified by:   JY
# @Last modified time: 2019-02-14T11:15:23+09:00
# @Copyright: JeeY

import copy
import time as ti

filename01 = 'train_dataset_raw_00.train'
filename02 = 'test_dataset_raw_00.test'

filename03 = 'train_dataset_raw_01.train'


full_result_list = list()

def make_one_dataset(data, buffer, stack): # data => elements of a word
    result = list()
    stack.append(['root', 0])
    for i,j in enumerate(data):
        temp = copy.deepcopy(j[2:])
        stack.append([buffer[0], int(j[0]), int(j[1]), temp])
        del buffer[0]
        one_line = list()
        if i == 0:
            one_line.append('root')
            one_line.append(temp)
            one_line.append('shift')
            result.append(one_line)
            continue
        one_line = list()
        del_list = list()
        for m,n in enumerate(reversed(stack), 1):
            one_line = list()
            if m == 1:
                continue
            if n[0] == 'root':
                if stack[-2][0] == 'root' and stack[-1][2] != 0:
                    one_line.append('root')
                    one_line.append(temp)
                    one_line.append('shift')
                    result.append(one_line)
                elif len(stack) > 2:
                    one_line.append(stack[-2][3])
                    one_line.append(stack[-1][3])
                    one_line.append('shift')
                    result.append(one_line)
                break
            # print(m, ' : ', stack, '\t\t', n)
            if stack[-1][1] == n[2]:
                one_line.append(stack[-2][3])
                one_line.append(stack[-1][3])
                one_line.append('left')
                result.append(one_line)
                for y,x in enumerate(stack):
                    if x[0] == n[0]:
                        del stack[y]
        if stack[-1][2] == 0 and len(stack) == 2:
            one_line = list()
            one_line.append('root')
            one_line.append(stack[-1][3])
            one_line.append('right')
            result.append(one_line)
            break
    return result

with open(filename01, 'r', encoding='utf-8') as f:
    ppara = 0
    switch = 1
    while True:
        line = f.readline()
        if not line: break
        line = line.split()
        if line == []:
            result = make_one_dataset(tmp_data, temp_buffer, temp_stack)
            modi_result = list()
            for i in result:
                for j in i:
                    if j == 'root' or j == 'shift' or j =='left' or j == 'right':
                        modi_result.append([j])
                        if j == 'shift' or j =='left' or j == 'right':
                            full_result_list.append(modi_result)
                            modi_result = list()
                        continue
                    modi_result.append(j)
            # full_result_list.append(modi_result)

            switch = 1
            # ppara += 1
            # if ppara == 1:
            #     print(result)
            #     for i,j in enumerate(full_result_list):
            #         print('%02d :\t'%i, j)
            #     print('\n\n')
            #     ti.sleep(100000)
            continue
        if switch == 1:
            temp_buffer = list()
            temp_stack = list()
            temp_buffer = list(line)
            switch = 0
            tmp_data = list()
            continue
        else:
            tmp_data.append(line)

# print(full_result_list[0])
with open(filename03, 'w', encoding='utf-8') as f:
    for i in full_result_list:
        for j in i:
            if j == ['left'] or j == ['shift'] or j == ['right']:
                word = '  '.join(j)
                f.write(word + '\n')
            else:
                word = '  '.join(j)
                f.write(word + '  #$%  ')
        if i[-1] == ['right']:
            f.write('\n\n')





















## endl
