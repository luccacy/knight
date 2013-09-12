'''
Created on 2013-8-29

@author: zhouyu
'''
from apscheduler.scheduler import Scheduler
from threading import Thread
import datetime
import tasks
import time
from knight.db import api as DB_API

TEN_MINUTE=10*60
THREE_HOUR=3*60*60
taskstore = tasks.TS.task_store
taskstore_lock = tasks.TS_LOCK
tasklist = tasks.TL
tasklist_lock = tasks.TL_LOCK

SCH = Scheduler(daemonic = False)
jobs = SCH.get_jobs()
if jobs is None:
    print 'no job'
else:
    print 'have job'

'''scheduler by apscheduler'''
def timer_task_scheduler():
    
    '''get all task from sensor tables'''
    try:
        all_sensor_refs = DB_API.sensor_get_all()
        if not all_sensor_refs:
            for sensor_ref in all_sensor_refs:
                port = sensor_ref.COM_N
                task = tasks.Task(port)
                
                if taskstore.has_key(port):
                    taskgroup = taskstore[port]
                else:
                    taskgroup = tasks.TaskGroup(port)
                
                taskgroup.tg_lock.acquire()    
                taskgroup.add_task(task, 'timer')
                taskgroup.tg_lock.release()
                
                taskstore_lock.acquire()
                taskstore.add_taskgroup(port,taskgroup)
                taskstore_lock.release()
                  
        '''start timer task in task store'''
        taskstore_lock.acquire()
        for group in taskstore:
            taskgroup = taskstore[group]
            port = taskgroup.port
            
            if taskgroup.timer_tasks_num <= 0 :
                continue
            
            taskgroup.tg_lock.acquire()
            timer_tasks = taskgroup.timer_tasks
            taskgroup.serial_open()
            for task in timer_tasks:
                task.start(taskgroup.serial)
                result = task.get_result()
                '''deal with result'''
                
                task.stop(taskgroup.serial)
                taskgroup.del_task(task, 'timer')
                    
            taskgroup.clear_tasks('timer')
            taskgroup.serial_close()
            
            taskgroup.tg_lock.release()
            
        taskstore_lock.release()        
    except:
        raise    
    
class TimerThread(Thread):   
    def __init__(self, taskgroup, task): 
        super(TimerThread, self).__init__()
    
    def run(self):
        old_timer_id = -1
        while True:
            timer_ids = (0,1,2)
            timer_id = 1
            internals = (24, 24*3, 24*7)
            interal = internals[timer_id]
            
            if timer_id == old_timer_id:
                time.sleep(THREE_HOUR)
                continue
            
            old_timer_id = timer_id
            
            jobs = SCH.get_jobs()
            if len(jobs) > 0:
                SCH.unschedule_job(timer_task_scheduler)
                         
            timestamp = time.time()
            timestruct = time.localtime(timestamp)
            cur_date = time.strftime('%Y-%m-%d', timestruct)
            run_time = ('%s 23:59:59' % cur_date)
        
            SCH.add_interval_job(timer_task_scheduler, hours=interal, start_date=run_time)
            SCH.start()
            
            time.sleep(THREE_HOUR)