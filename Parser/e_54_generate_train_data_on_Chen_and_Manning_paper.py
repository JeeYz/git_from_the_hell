# @Author: J.Y.
# @Date:   2019-03-04T14:23:20+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-09T23:50:12+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import time
import copy
import sys

sys.path.append(r'.\module')

import e_36_module_0 as mod0
import e_38_module_1 as mod1
import e_56_module_2 as mod2
import e_57_module_3 as mod3

filename2 = 'raw_train_dataset_00.train'
filename3 = 'raw_train_dataset_01.train'
# filename2 = 'result_07.result'

full_data = mod1.make_full_initial_raw_dataset(filename2)
# arc_data = mod2.making_arc_list(filename4)
print('full_data complete...')

full_train_input = list()
full_train_label = list()
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
                ##
                # print(len(one_data))
                temp = mod2.making_result_data(one_data, word_element_list)
                del one_data
                one_train_input.append(temp)

                transit = mod2.select_trainsition(stack_list, word_element_list,
                                                    head.childlist[0].word)
                ##
                # print('&&&& : ', transit)
                one_train_label.append(transit[0])

                # print('stack list : ', stack_list, transit, '\n')
                # print('buffer list : ', buffer_list, '\n')

                if transit[0] == 'shift':
                    stack_list.insert(0, str(buffer_list[0]))
                    del buffer_list[0]
                    break
                elif transit[0] == 'left':
                    del stack_list[transit[1]]
                else:
                    del stack_list[0]
                    break

    full_train_input.append(one_train_input)
    full_train_label.append(one_train_label)
    del one_train_input
    del one_train_label
    #########debuging sessino#################
    for w,z in enumerate(full_train_input[k]):
        if len(z) != 48:
            print(w, z, len(z), '\n\n')
    ##########################################
    # for z in full_train_label[k]:
    #     print(z)

    if len(full_train_input) != len(full_train_label):
        print(len(full_train_input[k]))
        print(len(full_train_label[k]))

    if k%1000 == 0:
        print('%d sents complete...\n' % k)


















## endl
