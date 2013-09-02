'''
Created on 2013-8-30

@author: zhouyu
'''

'''
a task group by serial port
'''
from threading import Thread 
from knight.common import serialutils 
import time

class Task(object):
    
    def __init__(self, port):
        self.port = port
        self.addr = None
        self.cmd = None
        self.output = None
        self.status = 'running'
        self.serial = None
        
    def start(self):
        self.serial = serialutils.SerialControl(5)
        self.serial.open()
        self.serial.start_thread()
        self.serial.write("#R#")
        time.sleep(1)
        self.output = self.serial.output       
    
    def stop(self):
        self.serial.close()
        self.status = 'finished'
    
    def get_result(self):
        return self.output
    
    def get_status(self):
        return self.status
    
class TaskGroup(object):
    
    def __init__(self, port):
        self.port = port
        self.custom_tasks = []
        self.timer_tasks = []
        self.timer_tasks_num = 0
        self.custom_tasks_num = 0 
        self.is_port_busy = False

    def add_task(self, task, type):
        if type == 'custom':
            self.custom_tasks.append(task)
            self.custom_tasks_num = self.custom_tasks_num + 1
        else:
            self.timer_tasks.append(task)
            self.timer_tasks_num = self.timer_tasks_num + 1
        
    def del_task(self, task, type):
        if type == 'custom':
            self.custom_tasks.remove(task)
            self.custom_tasks_num = self.custom_tasks_num - 1
        else:
            self.timer_tasks.remove(task)
            self.timer_tasks_num = self.timer_tasks_num - 1
        
    def set_port_status(self, status):
        '''True : busy, False : idle'''
        self.is_port_busy = status
    
    def get_port_status(self, status):
        return self.is_port_busy

 
class TaskStore(object):
    
    def __init__(self):
        self.task_store = {}
        
    def add_taskgroup(self, task_port, taskgroup):
        self.task_store[task_port] = taskgroup
        
    def del_taskgroup(self, task_port):
        return self.task_store.pop(task_port)
    
    def get_taskstore(self):
        return self.task_store
    
TS = TaskStore()
    