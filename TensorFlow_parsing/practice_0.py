# @Author: J.Y.
# @Date:   2019-03-20T15:32:21+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-20T15:45:07+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

# fn0 = 'd:/Program_Data/result_train_dataset_000.train'
#
# with open(fn0, 'r', encoding='utf-8') as f:
#     while True:
#         line = f.readline()
#         if not line:break
#         line = line.split()

import numpy as np

a = np.random.uniform(-1.0, 1.0, (10, 10))
b = list()
b.append(a[0])
b.append(a[5])
print(b)

print('\n\n')

b.extend(a[1])
print(b)

print('\n\n')

c = list()
c.extend(a[2])
c.extend(a[3])

print(c)
















## endl
