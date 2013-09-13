'''
Created on 2013-8-30

@author: zhouyu
'''

import tasks
import time
from knight.db import api as DB_API
from threading import Thread

TEN_MINUTE=10*60
taskstore = tasks.TS.task_store
taskstore_instance = tasks.TS
taskstore_lock = tasks.TS_LOCK
tasklist = tasks.TL
tasklist_lock = tasks.TL_LOCK

'''run in thread'''
def custum_task_scheduler():
    while True:
        '''add all task in tasklist to taskstore'''
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
        del tasklist[:]
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
                
            taskgroup.tg_lock.acquire()
            custom_tasks = taskgroup.custom_tasks
            taskgroup.serial_open()
            print('taskgroup : %s' % taskgroup)
            print('custom tasks : %s' % custom_tasks)
            for task in custom_tasks:
                print 'start task in scheduler'
                print task.port
                task.start(taskgroup.serial)
                result = task.get_result()
                '''deal with result'''
                print 'get result int scheduler'
                time.sleep(10)
                
                task.stop(taskgroup.serial)
            
            taskgroup.clear_tasks('custom')
                
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
        
        tasks = self.taskgroup.custom_tasks
        for task in tasks:
            task.start()
            result = task.get_result()

            time.sleep(10)
                
            task.stop(self.taskgroup.serial)
            
        self.task.start(self.taskgroup.serial)
            
        print 'get task result'
        result = self.task.get_result()
        '''deal with result'''
            
        self.task.stop(self.taskgroup.serial)
        self.taskgroup.serial_close()
        
        self.taskgroup.tg_lock.release()   
                           
                
            
        