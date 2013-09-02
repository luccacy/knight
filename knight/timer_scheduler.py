'''
Created on 2013-8-29

@author: zhouyu
'''
from apscheduler.scheduler import Scheduler
import datetime
import time
sch = Scheduler(daemonic = False)

def alarm():
    print 'alarm'

#alarm_time = time.time() + datetime.timedelta(seconds=2)
print time.ctime()    
alarm_time=datetime.time()
print alarm_time
sch.add_date_job(alarm, alarm_time, name='alarm1')

try:
    sch.start()
except:
    raise