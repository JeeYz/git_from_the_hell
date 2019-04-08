# @Author: J.Y.
# @Date:   2019-04-04T14:30:17+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-04-08T17:05:34+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import numpy as np
import h5py
filename = 'd:/Program_Data/model_weights_k_3.h5'

with h5py.File(filename, 'r') as f:
    # List all groups
    print("Keys: %s" % f.keys())
    print('\n')

    a_group_key = list(f.keys())
    print(a_group_key)
    print('\n')
    # Get the data
    
    data_set = f['embedding_1']
    # data_set.encode('utf-8')
    print(data_set)
    print('\n')

    b = f.get('dense_1')
    print(b)
    print('\n')















## endl
