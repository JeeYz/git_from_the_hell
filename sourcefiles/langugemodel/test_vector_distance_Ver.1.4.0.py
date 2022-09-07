# @Author: JayY
# @Date:   2018-12-11T09:57:30+09:00
# @Filename: test_vector_distance_Ver.1.4.0.py
# @Last modified by:   JayY
# @Last modified time: 2018-12-11T10:16:21+09:00
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

# ============< Ver.1.4.0 >==================================
# this is for sejong written
# ===========================================================


import numpy as np
import tensorflow as tf
import sys
sys.setrecursionlimit(50000)

word_vector_size = 300
result_words_num = 20
word_dict = dict()
search_dict = dict()

num_lines = 0

filename00 = './data/sejong/written/result_03.txt'

with open(filename00, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline().split()
        if not line: break
        num_lines += 1
        word_dict[line[0]] = line[1]
        search_dict[line[1]] = line[0]

fp_var = tf.gfile.FastGFile('X_input_variables_sejong_.txt', mode='a')

given_word_index = tf.placeholder(dtype=tf.int32, shape=[1], name='index_for_given')
X_input = tf.Variable(tf.zeros([num_lines, word_vector_size], dtype=tf.float32),
                      dtype=tf.float32, name='X_for_word_vector')

saver = tf.train.Saver()
given_var = tf.nn.embedding_lookup(X_input, given_word_index)
#print_result_embedding = tf.Print(given_var, [given_var], 'given_vector')
distance = tf.reduce_sum(tf.abs(tf.add(X_input, tf.negative(given_var))), reduction_indices=1)
#predict = tf.argmin(distance, 0)
predict = tf.nn.top_k(-distance, result_words_num)
init = tf.global_variables_initializer()

with tf.Session() as session:
    # saver = tf.train.Saver()
    session.run(init)
    saver.restore(session, tf.train.latest_checkpoint('skip_gram'))
    fp_var.write(str(session.run(X_input)) + str('\n\n'))
    print(session.run(X_input))
    while True:
        inputed_word = input("찾을 단어를 입력 : ")
        if inputed_word == 'stop': break
        if inputed_word not in word_dict:
            print("please insert again.")
            continue
        inputed_word_index = word_dict.get(inputed_word)
        predict_word = session.run(predict, feed_dict={given_word_index: [inputed_word_index]})
        # print(session.run(given_var))
        # session.run(print_result_embedding)
        # print(predict_word.indices)

        for a_pred in predict_word.indices:
            print(search_dict.get(str(a_pred)))
