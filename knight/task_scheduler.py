'''
Created on 2013-8-30

@author: zhouyu
'''

import tasks
import time
from knight.db import api as DB_API
from threading import Thread
from knight.common import logger

LOG = logger.get_logger(__name__)
TEN_MINUTE=10*60
taskstore = tasks.TS.task_store
taskstore_instance = tasks.TS
taskstore_lock = tasks.TS_LOCK


'''run in thread'''
def custum_task_scheduler():
    while True:
        '''add all task in tasklist to taskstore'''
        tasklist = tasks.TL
        tasklist_lock = tasks.TL_LOCK
        tasklist_lock.acquire()
        if len(tasklist) > 0 :
            print 'push tasklist to taskstore'
            for task_item in tasklist:
                port = task_item.port
                if taskstore.has_key(port):
                    taskgroup = taskstore[port]
                else:
                    taskgroup = tasks.TaskGroup(port)
                
                taskgroup.tg_lock.acquire()    
                taskgroup.add_task(task_item, 'custom')
                taskgroup.tg_lock.release()
                
                taskstore_lock.acquire()
                taskstore_instance.add_taskgroup(port,taskgroup)
                taskstore_lock.release()
        tasks.TL = []
        tasklist_lock.release()    
        
        print 'start all custom tasks in scheduler'
        '''start all custom tasks in taskstore'''
        print('taskstore : %s' % taskstore)
        taskstore_lock.acquire()
        for group in taskstore:
            taskgroup = taskstore[group]
            port = taskgroup.port
            
            
            if taskgroup.custom_tasks_num <= 0 :
                continue
            
            print('=======lock: %d' % taskgroup.custom_tasks_num)
            taskgroup.tg_lock.acquire()
            print('=======lock after')
            
            custom_tasks = taskgroup.custom_tasks
            if taskgroup.serial_open() is None:
                LOG.error('failed ot open serial : %d', port)
                continue
            print('=======taskgroup : %s' % taskgroup)
            print('=======custom tasks num : %d' % taskgroup.custom_tasks_num)
            for task in custom_tasks:
                print('=======run sample1: %d' % taskgroup.custom_tasks_num)
                task.run_first_sample_step1(taskgroup.serial)
                
            time.sleep(1)
            
            for task in custom_tasks:
                print('=======run sample2: %d' % taskgroup.custom_tasks_num)
                task.run_first_sample_step2(taskgroup.serial)
            
            print('clear taskgroup : %s' % (taskgroup.port))
            taskgroup.clear_tasks('custom')
            print('taskgroup num  : %d' % (taskgroup.custom_tasks_num))
                
            taskgroup.serial_close()
            taskgroup.tg_lock.release()
        taskstore_lock.release()
                        
        time.sleep(3)
  
class TaskThread(Thread):   
    def __init__(self, taskgroup, task): 
        super(TaskThread, self).__init__()
        self.taskgroup = taskgroup
        self.task = task
    
    '''we dont add task to tastgroup or taskstore
       we just get the taskgroup lock'''
    def run(self):
        print 'start task'
        '''start task'''
        self.taskgroup.tg_lock.acquire()
        self.taskgroup.serial_open()
        self.task.start(self.taskgroup.serial)
            
        print 'get task result'
        result = self.task.get_result()
        '''deal with result'''
            
        self.task.stop(self.taskgroup.serial)
        self.taskgroup.serial_close()
        
        self.taskgroup.tg_lock.release()            
                        
class TaskGroupThread(Thread):
    def __init__(self, taskgroup):
        super(TaskGroupThread, self).__init__()
        self.taskgroup = taskgroup
        
    def run(self):
        self.taskgroup.tg_lock.acquire()
        self.taskgroup.serial_open()
        
        custom_tasks = self.taskgroup.custom_tasks
        
        for task in custom_tasks:
            task.run_first_sample_step1(self.taskgroup.serial)
                
        time.sleep(10)
            
        for task in custom_tasks:
            task.run_first_sample_step2(self.taskgroup.serial)
            
        self.taskgroup.clear_tasks('custom')
          
        self.taskgroup.serial_close()
        
        self.taskgroup.tg_lock.release()
        print '=================taskgroupthread release lock'   
                           
                
            
        