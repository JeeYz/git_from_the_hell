# @Author: Jay
# @Date:   2018-10-29T17:17:33+09:00
# @Filename: find_out_distance_01.py
# @Last modified by:   Jay
# @Last modified time: 2018-11-01T18:15:38+09:00
# @Copyright: JayY



import numpy as np
import math

word_vec = 300

a = np.random.uniform(-1.0, 1.0, [word_vec])
b = np.random.uniform(-1.0, 1.0, [word_vec])

sum = 0
for j in range(100):
    for i in range(word_vec):
        c = math.sqrt(math.pow((b[i] - a[i]), 2))
        sum += c

print(sum)
