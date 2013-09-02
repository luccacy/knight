'''
Created on 2013-8-30

@author: zhouyu
'''

import tasks
import time

TEN_MINUTE=10*60

'''run in thread'''
def custum_task_scheduler():
    while True:
        taskstore = tasks.TS.task_store
        for group in taskstore:
            taskgroup = taskstore[group]
            port = taskgroup.port
            custom_tasks = taskgroup.custom_tasks
            for task in custom_tasks:
                '''wait for port idle'''
                while True:
                    port_status = taskgroup.get_port_status()
                    if  port_status == False:
                        task.start()
                        '''wait for output'''
                        while True:
                            '''fix me to decide if task end'''
                            if(task.get_result() == None):
                                time.sleep(3)
                            else:
                                result = task.get_result
                                taskgroup.set_port_status(False)
                    else:
                        time.sleep(10)
                        
        time.sleep(TEN_MINUTE)
  
'''scheduler by apscheduler'''
def timer_task_scheduler():
    
    taskstore = tasks.TaskStore.get_taskstore()
    for group in taskstore:
        taskgroup = taskstore[group]
        port = taskgroup.port
        timer_tasks = taskgroup.timer_tasks
        for task in timer_tasks:
            task.start()
            while True:
                '''fix me to decide if task end'''
                if(task.get_result() == None):
                    time.sleep(3)
                else:
                    result = task.get_result
                        
                        
                        
                        
                
            
        