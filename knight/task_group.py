'''
Created on 2013-8-30

@author: zhouyu
'''

'''
a task group by serial port
'''

class TaskGroup(object):
    
    def __init__(self, port):
        self.port = port
        self.tasks = []
        self.has_task_running = False
        
    
    def add_task(self, task):
        self.tasks.append(task)
        
    def del_task(self, task):
        self.tasks.remove(task)
 
        