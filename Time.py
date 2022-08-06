from time import time
from datetime import datetime


d = datetime(1,1,1).now()
print(d)

d = datetime(1,1,1).now()
print('{}:{:02d} {}/{}/{}'.format(d.hour,d.minute,d.month,d.day,d.year))

