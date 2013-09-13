'''
Created on 2013-9-1

@author: zhouyu
'''
from knight.db.sqlalchemy.session import get_session
from knight.db.sqlalchemy import models
from knight.common import exception

def model_query(model, *args, **kwargs):
    """Query helper that accounts for context's `read_deleted` field.
    """
    session = kwargs.get('session') or get_session()
    query = session.query(model, *args)

    return query

def sensor_create(values, session=None):
    sensor_ref = models.Sensor()
    
    sensor_ref.update(values)
    if session is None:
        session = get_session()
    sensor_ref.save(session=session)
    return sensor_ref

def sensor_get_by_id(sensor_id, session=None):
    if session is None:
        session = get_session()
    result = model_query(models.Sensor, session=session).\
                     filter_by(RECORD_ID=sensor_id).\
                     first()
    if not result:
        raise exception.SensorNotFound()

    return result

def sensor_get_all(session=None):
    if session is None:
        session = get_session()
    
    query = model_query(models.Sensor, session)
    query.all()
    

def pickdata_create(values, session=None):
    pickdata_ref = models.Pickdata()
    
    pickdata_ref.update(values)
    if session is None:
        session = get_session()
    pickdata_ref.save(session=session)
    return pickdata_ref

def pickdata_get(pickdata_id, session=None):
    if session is None:
        session = get_session()
    result = model_query(models.Pickdata, session=session).\
                     filter_by(RECORD_ID=pickdata_id).\
                     first()
    if not result:
        raise exception.SensorNotFound()

    return result

def pickdata_update(pickdata_id, values, session=None):
    if session is None:
        session = get_session()
        
    pickdata_ref = pickdata_get(pickdata_id, session)
    pickdata_ref.update(values)
    pickdata_ref.save(session=session)
    
def warning_get_by_id(warning_id, session=None):
    if session is None:
        session = get_session()
        
    result = model_query(models.Pickdata, session=session).\
                     filter_by(RECORD_ID=warning_id).\
                     first()   
    if not result:
        raise exception.SensorNotFound()
    
    return result

def warning_get_by_basetype(base_type, session=None):
    if session is None:
        session = get_session()
        
    result = model_query(models.Pickdata, session=session).\
                     filter_by(BASE_TYPE=base_type).\
                     first()   
    if not result:
        raise exception.SensorNotFound()
    
    return result

def battery_create(values, session=None):
    battery_ref = models.Battery()
    
    if session is None:
        session = get_session()
    
    battery_ref.update(values)
    battery_ref.save(session=session)
    return battery_ref

'''group_id : string 111111-1
   serial_num : battery serial num'''
def  battery_get_by_groupid_and_serialnum(group_id, serial_num, session=None):
    if session is None:
        session = get_session()
        
    result = model_query(models.Battery, session=session).\
                filter_by(GROUP_V = group_id).\
                filter_by(SERIAL_N = serial_num).\
                first()
                
    if not result:
        raise exception.SensorNotFound()
    
    return result

'''group_id : string 111111-1
   serial_num : battery serial num'''
def  battery_get_count_by_status(group_id, serial_num, status_n,session=None):
    if session is None:
        session = get_session()
        
    result = model_query(models.Battery, session=session).\
                filter_by(GROUP_V = group_id).\
                filter_by(SERIAL_N = serial_num).\
                filter_by(STATUS_N = status_n).\
                first()
                
    if not result:
        raise exception.SensorNotFound()
    
    return result

def battery_update(group_id, serial_num, values, session=None):
    
    if session is None:
        session = get_session()
        
    battery_ref = battery_get_by_groupid_and_serialnum(group_id, serial_num, session)
    
    battery_ref.update(values)
    battery_ref.save(session=session)
    
def batterys_get_by_id(batterys_id, session=None):
    
    if session is None:
        session = get_session()
        
    result = model_query(models.Batterys, session=session).\
                    filter_by(RECORD_ID = batterys_id).\
                    first()
                    
    if not result:
        raise exception.SensorNotFound()
    
    return result

def batterys_update(batterys_id, values, session=None):
     
    if session is None:
        session = get_session()
        
    batterys_ref = batterys_get_by_id(batterys_id, session)
    
    batterys_ref.update(values)
    batterys_ref.save(session=session)

def btrundata_create(values, session=None):
    btrundata_ref = models.Btrundata()
    
    if session is None:
        session = get_session()
    
    btrundata_ref.update(values)
    btrundata_ref.save(session=session)
    return btrundata_ref


def dictbattery_get_by_id(dictbattery_id, session=None):
    if session is None:
        session = get_session()
        
    result = model_query(models.Dictbattery, session=session).\
                    filter_by(RECORD_ID = dictbattery_id).\
                    first()
                    
    if not result:
        raise exception.SensorNotFound()
    
    return result

'''  
sensor = {'SENSORNAME_V':'sensor',
          'GROUPNAME_V' : 'group'}

sensor_create(sensor)   
'''

