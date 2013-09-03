'''
Created on 2013-9-3

@author: zhouyu
'''
from apscheduler.scheduler import Scheduler
from threading import Thread
from knight.db import api as DB_API
from knight import tasks
import time


taskstore_instance = tasks.TS
taskstore_lock = tasks.LOCK

def do_task():
    pass
    
def do_a_task_in_thread():
    thread = Thread(do_task, name='do_task')
    thread.start()

def timer_job():    
    '''load all sensor and push to taskstore'''
    all_sensors = DB_API.sensor_get_all()

    for sensor in all_sensors:
        task = tasks.Task(sensor.COM_N)
        task.addr = sensor.SENSOR_ADDR_N
        task.group_id = sensor.GROUPNAME_V
        task.sensor_n = sensor.SENSOR_N
        task.cmd = "#R#"
        
        taskstore_lock.acquire()
        taskstore = taskstore_instance.task_store
        port = task.port
        if taskstore.has_key(port):
            taskgroup = taskstore[port]
            taskgroup.add_task(task, 'timer')
        else:
            taskgroup = tasks.TaskGroup(port)
            taskgroup.add_task(task,'timer')
            taskstore_instance.add_taskgroup(port, taskgroup)
        taskstore_lock.release()
            
    '''foreach task, decide it to run'''
    for group in taskstore:
        taskgroup = taskstore[group]
        port = taskgroup.port
        serial_lock = taskgroup.serial_lock
        timer_tasks = taskgroup.timer_tasks
        serial_lock.acquire()
        serial_inst = taskgroup.serial_open()
        for task in timer_tasks:
            task.start(serial_inst)
            while True:
                '''fix me to decide if task end'''
                if(task.get_result() == None):
                    time.sleep(3)
                else:
                    result = task.get_result
        taskgroup.serial_close()
        serial_lock.release()

sched = Scheduler()
sched.start()

'''run once every day'''
sched.add_cron_job(timer_job, day_of_week='0-6', hour=0, minute=0)

'''run once every week'''
sched.add_cron_job(timer_job, day_of_week='0', hour=0, minute=0)

'''run once every three day'''
sched.add_cron_job(timer_job, day_of_week='mon,wed,sun', hour=0, minute=0)