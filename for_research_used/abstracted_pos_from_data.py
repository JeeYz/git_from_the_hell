# @Author: JayY
# @Date:   2018-11-07T10:46:10+09:00
# @Filename: abstracted_pos_from_data.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-07T13:00:24+09:00
# @Copyright: JayY

pos_list = list()

# abstract pos from file
fp = open('./data/korean_wiki/abstracted_pos_list.txt', 'w', encoding='utf-8')

# read file
with open('./data/korean_wiki/korean_wiki_raw_data_poses_tmp.txt', 'r', encoding='utf-8') as f:
    data = f.read().split()
    for a_pos in data:
        if a_pos in pos_list:
            continue
        pos_list.append(a_pos)

print(pos_list)
fp.write('\n'.join(pos_list))
