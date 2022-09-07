# @Author: JayY
# @Date:   2018-11-07T10:37:46+09:00
# @Filename: generating_dataset_sequence.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-07T15:48:13+09:00
# @Copyright: JayY


# ++++++++++++++++++++++++++++++++++++++++++++
# *** ORDER ***
#
# 1. add pad_start, pad_end to front of the sentence and tail of the sentence.
# 2. make first word data file.
# 3. and then second word data file adding frequency.
# 4. reduce word dictionary by frequency
# 5. change sentence dataset using reduced word dictionary
# 6. make huffman tree and write results of them
# 7. generate train data
