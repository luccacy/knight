'''
Created on 2013-9-1

@author: zhouyu
'''

from knight.db.sqlalchemy import api
from knight.db.sqlalchemy import store


IMPL = api

def sensor_get_all():
    return IMPL.sensor_get_all()

def sensor_get_by_id(sensor_id):
    return IMPL.sensor_get_by_id(sensor_id)

def cyclesetting_get_cycle(id=1):
    return IMPL.cyclesetting_get_cycle(id)

def store_to_db(batterys_id, sensor_n, values):
    return store.store_to_db(batterys_id, sensor_n, values)