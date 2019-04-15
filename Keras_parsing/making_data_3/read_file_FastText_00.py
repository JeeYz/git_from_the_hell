# @Author: J.Y.
# @Date:   2019-04-15T09:39:11+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-15T14:14:43+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

ft_file = 'D:/Program_Data/fastText/fastText-0.1.0/result/model_dim_128_skipgram_2.vec'
f_word = 'd:/Program_Data/result_raw_words_list_00.words'

w_matrix = list()
temp = list()
word_list = list()
with open(ft_file, 'r', encoding='utf') as f:
    switch = 0
    while True:
        line = f.readline()
        if not line:break
        line = line.split()
        if line[0] == '</s>':
            continue
        if switch == 0:
            switch = 1
        else:
            temp.append(line[0])
temp.sort()
# for i in temp:
#     a = np.array(i[1:])
#     w_matrix.append(a)

with open(f_word, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:break
        line = line.split()
        word_list.append(line[0])

print(len(word_list))
print(len(temp))

# for i in temp:
#     if i not in word_list:
#         print(i)
#
# print('\n=======================\n')
#
# for i in word_list:
#     if i not in temp:
#         print(i)

for i,j in enumerate(temp):
    if j != word_list[i]:
        print(j)











## endl
