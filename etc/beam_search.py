
import random
import copy


input_data = list()

for i in range(10):
    temp_val = random.random()
    input_data.append(temp_val)


print(input_data)

beam_search_size = 3


def gen_beam_list(input_data):
    arrange_list = copy.deepcopy(input_data)
    global beam_search_size

    idx_num = 0
    flag_num = 0

    while True:
        target_idx = idx_num+1

        if arrange_list[idx_num] < arrange_list[target_idx]:
            curr_num = arrange_list[idx_num]
            next_num = arrange_list[target_idx]

            arrange_list[idx_num] = next_num
            arrange_list[target_idx] = curr_num

            flag_num += 1

        idx_num += 1
        if idx_num == (len(arrange_list)-1):
            idx_num = 0

            if flag_num == 0:
                break
            else:
                flag_num = 0

    return arrange_list[:beam_search_size]


first_beam_list = gen_beam_list(input_data)
print(first_beam_list)


idx_list = list()


for one_val in first_beam_list:
    temp_idx = input_data.index(one_val)
    idx_list.append(temp_idx)

print(idx_list)


sequence_lenth = 5


result_list = list()


for i in range(beam_search_size):
    temp_dict = dict()
    temp_dict['index_list'] = list()
    temp_dict['probability'] = 0.

    temp_dict['index_list'].append(idx_list[i])
    temp_dict['probability'] = input_data[idx_list[i]]

    result_list.append(temp_dict)


def gen_random_list():
    return_list = list()
    for i in range(10):
        return_list.append(random.random())
    return return_list 


def gen_index_list_for_beam(input_val_list, origin_data):
    idx_list = list()

    for one_val in input_val_list:
        temp_idx = origin_data.index(one_val)
        idx_list.append(temp_idx)

    return idx_list


for i in range(sequence_lenth-1):
    print("{}th sequence....".format(i))
    limit_loop_num = len(result_list)
    print(limit_loop_num)

    for n in range(limit_loop_num):
        one_dict = result_list[n]
        origin_dict = copy.deepcopy(one_dict)

        input_list = gen_random_list()
        temp_val_list = gen_beam_list(input_list)
        target_index_list = gen_index_list_for_beam(temp_val_list, input_list)

        for j, one_idx in enumerate(target_index_list):
            if j == 0:
                one_dict['index_list'].append(one_idx) 
                one_dict['probability'] *= input_list[one_idx]
            else:
                temp_dict = copy.deepcopy(origin_dict)
                temp_dict['index_list'].append(one_idx) 
                temp_dict['probability'] *= input_list[one_idx]
                result_list.append(temp_dict)



def decide_result(input_full):
    max_val = 0.
    max_index = 0

    for i, one_dict in enumerate(input_full):
        if max_val < one_dict['probability']:
            max_val = one_dict['probability']
            max_index = i

    return max_val, input_full[max_index] 
        


result_val, result_seq = decide_result(result_list)

print("final result : {pro}, {sequence}".format(pro=result_val, sequence=result_seq['index_list']))

















