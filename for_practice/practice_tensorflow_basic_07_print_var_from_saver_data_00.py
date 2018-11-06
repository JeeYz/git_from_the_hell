# @Author: Jay
# @Date:   2018-11-01T09:25:56+09:00
# @Filename: print_tf_variables_from_saver_data_00.py
# @Last modified by:   JeeYz
# @Last modified time: 2018-11-02T14:00:13+09:00
# @Copyright: JayY



import tensorflow as tf
import io

num_lines = 0
word_vector_size = 300
with open('d:/Programming/result_03.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    num_lines = len(data)

#fp_var = tf.gfile.FastGFile('tensor_variable_from_saver_00.txt', 'w')
X_input = tf.Variable(tf.zeros([num_lines, word_vector_size], dtype=tf.float32),
                      dtype=tf.float32, name='X_for_word_vector')
saver = tf.train.Saver()
print_word_vector = tf.Print(X_input, [X_input], "Variable for word vector")
#print_out_file = tf.write_file('tensor_variable_from_saver_00.txt', X_input)
init = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(init)
    saver.restore(session, tf.train.latest_checkpoint('d:/Programming/skip_gram'))
    session.run(print_word_vector)
    print(session.run(X_input))
