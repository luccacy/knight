'''
Created on 2013-8-29

@author: zhouyu
'''
from knight import tasks
from knight import timer_scheduler
from knight import task_scheduler
from knight.db import api as DB_API


taskstore = tasks.TS.task_store
taskstore_instance = tasks.TS
taskstore_lock = tasks.TS_LOCK
tasklist = tasks.TL
tasklist_lock = tasks.TL_LOCK

sched = timer_scheduler.SCH

class TaskController(object):
    def __init__(self):
        pass
    
    def list_tasks(self):
        print 'list tasks'
        
        for group in taskstore:
            taskgroup = taskstore[group]
            port = taskgroup.port
            custom_tasks = taskgroup.custom_tasks
            
            print('taskgroup port : %s' % taskgroup.port)
            print('taskgroup custom tasks num : %d' % taskgroup.custom_tasks_num)
            
            for task in custom_tasks:
                print('task port : %s' % task.port)
        
    def create_task(self, args):
        
        sensor_ids = args.pop('sensor_ids')
        sensor_id_list = sensor_ids.split(',')
        taskstore_tmp = tasks.TaskStore()
        tasks = []
        
        '''from sensor ids to tasks'''
        for sensor_id in sensor_id_list:
            sensor_ref = DB_API.sensor_get_by_id(sensor_id)
            task = tasks.Task(sensor_ref.COM_N)
            task.addr = sensor_ref.SENSOR_ADDR_N
            tasks.append(task)
            
        '''store all tasks to taskstore_tmp'''
        for task in tasks:
            port = task.port
            if taskstore_tmp.has_key(port):
                taskgroup_tmp = taskstore_tmp[port]
            else:
                taskgroup_tmp = tasks.TaskGroup(port)  
                taskstore_tmp.add_taskgroup(port, taskgroup_tmp)
            taskgroup_tmp.add_task(task, 'custom')
        
        '''iterate all taskgroup_tmp, if taskstore have waiting tasks
        push taskgroup_tmp' cunstom_tasks list to tasklist, if don't have,
        run the taskgroup_tmp in thread'''
        for port in taskstore_tmp:
            taskgroup_tmp = taskstore_tmp[port]
            if taskstore.has_key(port):
                taskgroup = taskstore[port]
                if taskgroup.custom_tasks_num > 0:
                    '''have waiting tasks, store tasks to waiting task list'''
                    tasklist_lock.acquire()
                    tasklist.extend(taskgroup_tmp.custom_tasks)
                    tasklist_lock.release()
                else:
                    '''don't have waiting tasks, start in thread'''
                    taskstore[port] = taskgroup_tmp
                    tg_thread = task_scheduler.TaskGroupThread(taskgroup_tmp)
                    tg_thread.start()
            else:
                '''don't have waiting tasks, start in thread'''
                taskstore[port] = taskgroup_tmp
                tg_thread = task_scheduler.TaskGroupThread(taskgroup_tmp)
                tg_thread.start()
                                                         
        return 200
#         port = args.pop('port')
#         task = tasks.Task(port)
#         taskgroup = None
#         action = ''
#         print 'create task'
#         '''
#         check if has the same task running
#         '''        
# 
#         if taskstore.has_key(port):
#             taskgroup = taskstore[port]
#             print taskgroup.custom_tasks_num
#             if taskgroup.custom_tasks_num > 0:
#                 action = 'waiting'
#             else:
#                 action = 'running'     
#         else:
#             action = 'running'
#             
#         print('action : %s' % action)
#             
#         if action == 'waiting':
#             print '''push to task list'''
#             tasklist_lock.acquire()
#             tasklist.append(task)
#             tasklist_lock.release()
#                 
#         elif action == 'running':
#             '''run in thread?'''
#             if taskgroup == None: 
#                 taskgroup = tasks.TaskGroup(port)
#                 
#             taskthread = task_scheduler.TaskThread(taskgroup, task)
#             taskthread.start()
            
    def create_timer(self):
        try:
            
            sched.add_cron_job(timer_scheduler.timer_task_scheduler, 
                               day_of_week='0-6', hour=0, minute=0)
            sched.start()
        except:
            raise
        
        
    def delete_timer(self):
        try:
            sched.unschedule_job(timer_scheduler.timer_task_scheduler) 
            sched.shutdown(wait=False)    
        except:
            raise                                  
    
    def delete_task(self):
        pass
    
    def get_task(self,id):
        print 'show task list'
        for task in tasklist:
            print task.port
        
    
    def update_task(self,id, args):
        for port in ('0','1','2','3','4'):
            for i in range(3):
                task = tasks.Task(port)
                tasklist.append(task)

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