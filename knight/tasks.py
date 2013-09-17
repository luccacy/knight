'''
Created on 2013-8-30

@author: zhouyu
'''

'''
a task group by serial port
'''
from threading import Thread, Lock
from knight.common import serialutils 
from knight.common import protocal
from knight.db import api as DB_API

import time

class Task(object):
    
    def __init__(self, port):
        self.port = port
        self.addr = None
        self.cmd = None
        self.output = None
        self.status = 'ok'
        self.serial = None
        self.group_id = None
        self.sensor_n = None
        self.sensor_id = None
        self.base_id = None
        self.user_id = None
        
    def exec_cmd(self, serial, cmd):

        cmd_str, recv_str = protocal.encode_cmd(cmd, self.addr)
        serial.write(cmd_str)
        time.sleep(3)

        self.output = serial.output
        result_dict = protocal.decode_result(self.output)
        
        return result_dict, recv_str
            
    def start(self, serial):
        serial.start_thread()
        
    def run_first_sample(self, serial):
        self.start(serial)
        
        '''sample1'''
        result = self.exec_cmd(serial, 'sample1')
        
        if result is not None:
            time.sleep(200)
            output = self.exec_cmd(serial, 'transport')
            result = protocal.decode_result(output)
            
            DB_API.store_to_db(self.group_id, self.sensor_n, self.sensor_id, self.user_id, result)
            
        self.stop(serial)
        
    def run_first_sample_step1(self, serial):
        self.start(serial)
        run_times = 0
        '''sample1'''
        while True:
            result_dict, right_result_str = self.exec_cmd(serial, 'sample1')
            result_data = result_dict['data']
            run_times += 1
            if result_data == right_result_str :
                break
            elif result_data != right_result_str and run_times == 3:
                self.status = 'sample1_failed'
                break
            else:
                time.sleep(1)
        
        return result_data
    
    def run_first_sample_step2(self, serial):
        run_times = 0
        while True:
            run_times += 1
            result_dict,null_str = self.exec_cmd(serial, 'transport')
            if result_dict['status'] == 0:
                break
            elif result_dict['status'] != 0 and run_times == 3:
                self.status = 'transport_failed'
                break
            else:
                time.sleep(1)
                       
        DB_API.store_to_db(self.group_id, self.sensor_n, self.sensor_id, self.user_id, result_dict, self.status)

        self.stop(serial)

    
    def stop(self, serial):
        serial.stop_thread()   
        self.output = None        
    
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
        self.serial = None
        self.tg_lock = Lock()

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
            
    def clear_tasks(self, type):
        if type == 'custom':
            del self.custom_tasks[:]            
            self.custom_tasks_num = 0
        else:
            del self.timer_tasks[:]            
            self.timer_tasks_num = 0
            
    def run_task(self, task):
        if not self.serial:
            raise 'serial does not opened!'
        task.start(self.serial)
            
    def serial_open(self):
#         self.serial = serialutils.SerialControl(5)
#         self.serial.open()
#         return self.serial     
        pass
    def serial_close(self):
#         self.serial.close()
#         self.status = 'finished'
        pass
        
    def set_port_status(self, status):
        '''True : busy, False : idle'''
        self.is_port_busy = status
    
    def get_port_status(self, status):
        return self.is_port_busy

 
class TaskStore(object):
    
    def __init__(self):
        self.task_store_lock = Lock()
        self.task_store = {}
        
    def add_taskgroup(self, task_port, taskgroup):
        self.task_store[task_port] = taskgroup
        
    def del_taskgroup(self, task_port):
        return self.task_store.pop(task_port)
    
    def get_taskstore(self):
        return self.task_store
    
TS = TaskStore()
TS_LOCK = TS.task_store_lock
TL = []
TL_LOCK = Lock()
    