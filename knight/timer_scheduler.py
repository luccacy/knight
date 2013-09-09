'''
Created on 2013-8-29

@author: zhouyu
'''
from apscheduler.scheduler import Scheduler
import datetime
import tasks
import time
from knight.db import api as DB_API

TEN_MINUTE=10*60
taskstore = tasks.TS.task_store
taskstore_lock = tasks.TS_LOCK
tasklist = tasks.TL
tasklist_lock = tasks.TL_LOCK

SCH = Scheduler(daemonic = False)

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