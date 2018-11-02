# @Author: JayY <JeeYz>
# @Date:   2018-10-30T10:12:01+09:00
# @Filename: print_time_of_now_01.py
# @Last modified by:   JeeYz
# @Last modified time: 2018-11-02T14:00:15+09:00
# @Copyright: JayY



import time
from datetime import datetime

now = datetime.now()
print(now)

now = datetime.now()
time.sleep(1)
late = datetime.now()
print(late-now)

print('\'hello, world\'')
