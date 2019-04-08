# @Author: J.Y.
# @Date:   2019-04-04T14:30:17+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-08T08:56:39+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import numpy as np
import h5py
filename = 'd:/Program_Data/model_weights_k_3.h5'
f = h5py.File(filename, 'r')

# List all groups
print("Keys: %s" % f.keys())
a_group_key = list(f.keys())[0]

# Get the data
data = list(f[a_group_key])
data_set = f['embedding_1']
print(data_set)

print(['dense_1'])

b = f.get('dense_1')
print(b)



## endl
