# @Author: J.Y.
# @Date:   2019-03-09T23:55:02+09:00
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-20T16:34:18+09:00
# @License: J.Y. JeeYz
# @Copyright: J.Y. JeeYz

import time
import copy
import sys

sys.path.append(r'.\module')

import e_36_module_0 as mod0
import e_38_module_1 as mod1
import e_56_module_2 as mod2
import e_57_module_3 as mod3

# filename2 = 'd:/Program_Data/raw_train_dataset_05.train'
# filename3 = 'd:/Program_Data/raw_train_dataset_06.train'

filename2 = 'd:/Program_Data/raw_test_dataset_01.test'
filename3 = 'd:/Program_Data/raw_test_dataset_02.test'
# filename2 = 'result_07.result'

full_data = mod1.make_full_initial_raw_dataset(filename2)
# arc_data = mod2.making_arc_list(filename4)
print('full_data complete...')

with open(filename3, 'w', encoding='utf-8') as f:
    for k,i in enumerate(full_data):
        one_train_input = list()
        one_train_label = list()

        stack_list = list()
        buffer_list = list()
        # if k == 1:
        #     time.sleep(10000)

        head = mod1.make_dependency_tree(i)
        # mod1.print_tree(head)
        word_element_list = mod2.making_word_elements_list(i)

        for m,n in enumerate(i):
            if m == 0 or m == 1:
                if m == 0:
                    buffer_list = copy.deepcopy(n)
                    stack_list.insert(0, 'ROOT')
                one_data = mod1.make_one_train_data(stack_list, buffer_list, head)
                # print(len(one_data))
                temp = mod2.making_result_data(one_data, word_element_list)
                del one_data
                one_train_input.append(temp)
                one_train_label.append('shift')

                temp = buffer_list[0]
                del buffer_list[0]
                stack_list.insert(0, temp)
            else:
                while True:
                    one_data = mod1.make_one_train_data(stack_list, buffer_list, head)

                    temp = mod2.making_result_data(one_data, word_element_list)
                    del one_data
                    one_train_input.append(temp)

                    transit = mod2.select_trainsition(stack_list, word_element_list,
                                                        head.childlist[0].word)

                    one_train_label.append(transit[0])

                    if transit[0] == 'shift':
                        stack_list.insert(0, str(buffer_list[0]))
                        del buffer_list[0]
                        break
                    elif transit[0] == 'left':
                        del stack_list[transit[1]]
                    else:
                        del stack_list[0]
                        break

        #########debuging sessino#################
        for z in one_train_input:
            if len(z) != 48:
                print(z)
        if len(one_train_input) != len(one_train_label):
            print('%d th sentence is not correct...' % k)
        ##########################################

        temp = list()
        for w,z in enumerate(one_train_input):
            line = str()
            for x,y in enumerate(z):
                a = '  '.join(y)
                line += a
                line += '\t##\t'
            line += str(one_train_label[w])
            temp.append(line)

        for z in temp:
            f.write(z + '\n')
        f.write('\n')
        if k%1000 == 0:
            print('%d sents complete...\n' % k)









## endl
