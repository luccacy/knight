'''
Created on 2013-8-29

@author: zhouyu
'''

class Task(object):
    
    def __init__(self, port):
        self.port = port
        self.addr = None
        self.cmd = None
        self.output = None
        self.status = 'running'
        
    def start(self):
        pass
    
    def stop(self):
        pass
    
    def get_result(self):
        return self.output
    
    def get_status(self):
        return self.status
    
    