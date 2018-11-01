
import tensorflow as tf
import io

num_lines = 0
word_vector_size = 300
with open('result_03.txt', 'r', encoding='utf-8') as f:
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
    saver.restore(session, tf.train.latest_checkpoint('skip_gram'))
    session.run(print_word_vector)
    print(session.run(X_input))
