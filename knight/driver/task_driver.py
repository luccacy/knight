'''
Created on 2013-8-29

@author: zhouyu
'''
from knight import tasks

taskstore_instance = tasks.TS
taskstore_lock = tasks.LOCK

class TaskController(object):
    def __init__(self):
        pass
    
    def list_tasks(self):
        print 'list tasks'
        taskstore = taskstore_instance.task_store
        for group in taskstore:
            taskgroup = taskstore[group]
            port = taskgroup.port
            custom_tasks = taskgroup.custom_tasks
            
            print('taskgroup port : %s' % taskgroup.port)
            print('taskgroup custom tasks num : %d' % taskgroup.custom_tasks_num)
            
            for task in custom_tasks:
                print('task port : %s' % task.port)
        
    def create_task(self, args):
        port = args.pop('port')
        task = tasks.Task(port)
        print 'create task'
        '''
        check if has the same task running
        '''
        taskstore_lock.acquire()
        taskstore = taskstore_instance.task_store
        if taskstore.has_key(port):
            taskgroup = taskstore[port]
            taskgroup.add_task(task, 'custom')
        else:
            taskgroup = tasks.TaskGroup(port)
            taskgroup.add_task(task,'custom')
            taskstore_instance.add_taskgroup(port, taskgroup)
        taskstore_lock.release()
    
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