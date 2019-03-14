# @Author: J.Y.
# @Date:   2019-03-13T16:34:16+09:00
# @Project: NLP
# @Last modified by:   J.Y.
# @Last modified time: 2019-03-14T12:01:04+09:00
# @License: JeeY
# @Copyright: J.Y. JeeY

import sys
sys.path.append(r'/module')

from keras import models
from keras import layers

import keras_module_0 as mod0

batch_size = 128

filepath = 'd:/Program_Data/'
filelist = list()

for i in range(1):
    filelist.append(filepath + 'result_train_dataset_%02d.train' %i)
filetuple = tuple(filelist)

for i in filetuple:
    mod1.generate_train_data(i, batch_size)











## endl
