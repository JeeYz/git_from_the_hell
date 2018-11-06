# @Author: JayY
# @Date:   2018-10-17T15:45:55+09:00
# @Filename: search_directory_function.py
# @Last modified by:   JayY
# @Last modified time: 2018-11-06T16:29:34+09:00
# @Copyright: JayY



'''
This is a practice file.
small functional moduleself.
simply search directorys
'''
import os

for (path, dir, files) in os.walk("./"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            #print("%s/%s" % (path, filename))
            pass

for path, dir, files in os.walk('./'):
    for filename in files:
        print("%s" % (path), "\t", "%s" % (filename))
