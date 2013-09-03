'''
Created on 2013-9-1

@author: zhouyu
'''

from knight.db.sqlalchemy import api


IMPL = api

def sensor_get_all():
    IMPL.sensor_get_all()