'''
Created on 2013-8-29

@author: zhouyu
'''
import task
import task_group

class TaskController(object):
    def __init__(self):
        pass
    
    def create_task(self, port):
        t = task.Task(port)
        '''
        check if has the same task running
        '''
        
        
        pass
    
    def delete_task(self):
        pass
    
    def show_task(self):
        pass
    
    def update_task(self):
        pass

'''
all_tasks = []
all_timer_tasks = None
all_custom_tasks = {}

all_custom_tasks = {'port' : task_group}
task1 = task.Task(1)
task2 = task.Task(2)

port = '3'

if all_custom_tasks.has_key(port):
    list = all_custom_tasks[port]
    t = task.Task(port)
    list.append(t)
else:
    list = []
    t = task.Task(port)
    list.append(t)
    all_custom_tasks[port] = list

print all_custom_tasks
print all_custom_tasks[port][0].get_status()

port = '3'
if all_custom_tasks.has_key(port):
    list = all_custom_tasks[port]
    t = task.Task(port)
    list.append(t)
else:
    list = []
    t = task.Task(port)
    list.append(t)
    all_custom_tasks[port] = list
    
print all_custom_tasks
print all_custom_tasks[port][1].get_status()

'''