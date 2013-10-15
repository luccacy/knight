'''
Created on 2013-10-15

@author: zhouyu
'''
from knight import tasks
import time


if __name__ == '__main__':
    com_n = 5
    addr = 10
    cmd = 'sample1'
    task = tasks.Task(com_n)
    task.addr = addr
    task.cmd = cmd
    
    taskgroup = tasks.TaskGroup(com_n)
    taskgroup.add_task(task, 'custom')
    
    if not taskgroup.serial_open():
        print 'failed to open serial'
        
    custom_tasks = taskgroup.custom_tasks
    for task_item in custom_tasks:
        task_item.run_first_sample_step1(taskgroup.serial)
        
    time.sleep(3)
    
    for task_item in custom_tasks:
        task_item.run_first_sample_step2(taskgroup.serial)
        
        
    taskgroup.clear_tasks('custom')
    taskgroup.serial_open()