# @Author: J.Y.
# @Date:   2019-03-04T14:23:20+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-08T15:46:58+09:00
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

filename2 = 'train_dataset_raw_00.train'
filename3 = 'result_05.result'
filename4 = 'temp_result_08_v02.temp'

full_data = mod1.make_full_initial_raw_dataset(filename2)
arc_data = mod2.making_arc_list(filename4)
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
    # node_list = mod1.print_tree(head, node_list)
    word_list = i[0]
    word_element_list = mod2.making_word_elements_list(i, arc_data[k])

    for m,n in enumerate(i):
        if m == 0 or m == 1:
            if m == 0:
                buffer_list = copy.deepcopy(n)
                stack_list.insert(0, 'ROOT')
            one_data = mod1.make_one_train_data(stack_list, buffer_list,
                                                word_element_list, head)
            ##
            # print(len(one_data))
            temp = mod2.making_result_data(one_data, word_element_list)
            one_train_input.append(temp)
            one_train_label.append('shift')

            temp = buffer_list[0]
            del buffer_list[0]
            stack_list.insert(0, temp)
        else:
            while True:
                one_data = mod1.make_one_train_data(stack_list, buffer_list,
                                                    word_element_list, head)
                ##
                # print(len(one_data))
                temp = mod2.making_result_data(one_data, word_element_list)
                one_train_input.append(temp)

                transit = mod2.select_trainsition(stack_list, word_element_list,
                                                    head.childlist[0].word)
                ##
                # print('&&&& : ', transit)
                one_train_label.append(transit[0])

                print('stack list : ', stack_list, transit, '\n')
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

    # if k%1000 == 0:
    #     print('1000 sents complete...\n')

# filename5 = 'train_dataset_raw_03.train'
# for i,j in enumerate(full_train_input):
#     for k,l in enumerate(j):
















## endl
