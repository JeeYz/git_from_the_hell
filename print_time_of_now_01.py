
import time
from datetime import datetime

now = datetime.now()
print(now)

now = datetime.now()
time.sleep(1)
late = datetime.now()
print(late-now)

print('\'hello, world\'')
