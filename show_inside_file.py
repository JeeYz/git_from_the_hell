# @Author: JayY
# @Date:   2018-11-05T14:02:53+09:00
# @Filename: show_inside_file.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T16:27:52+09:00
# @Copyright: JayY

# it is just for show inside file
# because some files are too big to read
# ==============================================

with open('korean_wiki_result_words_00.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        print(line)
