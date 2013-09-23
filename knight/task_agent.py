'''
Created on 2013-8-31

@author: zhouyu
'''
import os
import sys

from knight.driver import task_driver

class TaskAgent(object):
    
    def __init__(self):
        self._driver = task_driver.TaskController()
        
    def list_tasks(self):
        return self._driver.list_tasks()
        
    def create_task(self, args):
        return self._driver.create_task(args)
    
    def delete_task(self, id):
        return self._driver.delete_task(id)
        
    def get_task(self, id):
        return self._driver.get_task(id)
        
    def update_task(self, id, args):
        return self._driver.update_task(id,args)
        
    def list_timers(self):
        return self._driver.list_timers()
        
    def create_timer(self, args):
        return self._driver.create_timer(args)
    
    def delete_timer(self, id):
        return self._driver.delete_timer(id)