# @Author: JayY
# @Date:   2018-11-08T12:34:54+09:00
# @Filename: test_vector_distance_Ver.1.0.0.py
# @Last modified by:   JayY
# @Last modified time: 2018-12-11T08:13:34+09:00
# @Copyright: JayY


# ============< Ver.1.0.0 >==================================
# this version is for korean wiki data file
# find out vector distance
# hierachical sofmax model
# ===========================================================

# ============< Ver.1.1.0 >==================================
# modified for nce model
# ===========================================================

# ============< Ver.1.2.0 >==================================
# modified for relation between two words
# find out meaning realtion between two words
# for example, capital and country
# ===========================================================

# ============< Ver.1.3.0 >==================================
# this is for KOREAN NEWS
# ===========================================================

# ============< Ver.2.1.0 >==================================
# this version is in cluding calculating direction
# of course, distance , too
# using korean wiki parameters
# ===========================================================



import numpy as np
import tensorflow as tf
import sys
sys.setrecursionlimit(50000)

word_vector_size = 300
result_words_num = 100
output_words = 10
num_of_test = 10

word_dict = dict()
search_dict = dict()

test_list_country = ['미국', '한국', '일본', '중국', '러시아', '독일', '영국', '베트남', '태국', '터키']

voca_size = 0

filename00 = './data/korean_wiki/korean_wiki_result_words_04_adding_index.txt'

with open(filename00, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline().split()
        if not line: break
        voca_size += 1
        word_dict[line[0]] = [line[-1], line[1]]
        search_dict[line[-1]] = line[0]


first_word_index = tf.placeholder(dtype=tf.int32, shape=[1], name='first_word_index_nce')
second_word_index = tf.placeholder(dtype=tf.int32, shape=[1], name='second_word_index_nce')
test_word_index = tf.placeholder(dtype=tf.int32, shape=[1], name='test_word_index_nce')

center_word_v = tf.Variable(tf.zeros([voca_size, word_vector_size], dtype=tf.float32),
                      dtype=tf.float32, name='center_word_variable')

saver_nce_skip = tf.train.Saver()
first_var = tf.nn.embedding_lookup(center_word_v, first_word_index)
second_var = tf.nn.embedding_lookup(center_word_v, second_word_index)
test_var = tf.nn.embedding_lookup(center_word_v, test_word_index)

distance0 = tf.reduce_sum(tf.abs(tf.add(first_var, tf.negative(second_var))), reduction_indices=1)
direction0 = tf.subtract(second_var, first_var)

distance1 = tf.reduce_sum(tf.abs(tf.add(center_word_v, tf.negative(test_var))), reduction_indices=1)
direction1 = tf.subtract(center_word_v, test_var)

gap_of_distance = tf.subtract(distance1, distance0)
gap_of_direction = tf.reduce_sum(tf.subtract(direction1, direction0), reduction_indices=1)

predict = tf.nn.top_k(-tf.add(gap_of_distance, gap_of_direction), result_words_num)
init = tf.global_variables_initializer()



with tf.Session() as session:
    # saver_nce_skip = tf.train.Saver()
    session.run(init)
    saver_nce_skip.restore(session, tf.train.latest_checkpoint('nce_korean_wiki'))
    # fp_var.write(str(session.run(center_word_v)) + str('\n\n'))
    print(session.run(center_word_v))
    while True:
        first_inputed_word = input("insert a word what you want : ")
        if first_inputed_word == 'stop': break
        if first_inputed_word not in word_dict:
            print("please insert again.")
            continue
        second_inputed_word = input("insert a word what you want : ")
        if second_inputed_word == 'stop': break
        if second_inputed_word not in word_dict:
            print("please insert again.")
            continue
        first_inputed_word_index = word_dict.get(first_inputed_word)[0]
        second_inputed_word_index = word_dict.get(second_inputed_word)[0]

        for a_country in test_list_country:
            test_inputed_word_index = word_dict.get(a_country)[0]
            predict_word = session.run(predict, feed_dict={first_word_index: [first_inputed_word_index],
                                                           second_word_index: [second_inputed_word_index],
                                                           test_word_index: [test_inputed_word_index]})

            para = 0
            for a_pred in predict_word.indices:
                temp_word = search_dict.get(str(a_pred))
                if word_dict.get(str(temp_word))[1] == "NNG":
                    print(a_country, '\t', temp_word)
                    para += 1
                if para == output_words:
                    break



















##
