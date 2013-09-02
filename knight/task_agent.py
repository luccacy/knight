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
        self._driver.list_tasks()
        
    def create_task(self, args):
        self._driver.create_task(args)
    
    def delete_task(self, id):
        self._driver.delete_task(id)
        
    def get_task(self, id):
        self._driver.get_task(id)