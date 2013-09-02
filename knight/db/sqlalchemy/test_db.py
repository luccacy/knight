from knight.db.sqlalchemy import api
from knight.db.sqlalchemy import models

volt = [2.21,2.22,2.23,2.24,2.25,2.26,2.27,2.28,2.29,2.30]
inner = [4.41,4.42,4.43,4.44,4.45,4.46,4.47,4.48,4.49,4.51]

'''get batterys by batterys_id'''
batterys_id = '111111-1'
batterys_ref = api.batterys_get_by_id(batterys_id)

'''get warning thread values by batterys base type'''
base_type = batterys_ref.BASE_TYPE
warning_ref = api.warning_get_by_basetype(base_type)
yellow_max_red = warning_ref.YELTHRMAXRED_N
yellow_max_yellow = warning_ref.YELTHRMAXYEL_N
green_max_yellow = warning_ref.GRETHRMAXYEL_N
green_max_red = warning_ref.GRETHRMAXRED_N

'''get dict battery type'''
dict_battery_id = batterys_ref.BATTERYTYPE_V
dict_battery_ref = api.dictbattery_get_by_id(dict_battery_id)
b0 = dict_battery_ref.B0
b1 = dict_battery_ref.B1
std_inner = dict_battery_ref.STDINNER_V
std_inner_yellow = dict_battery_ref.YELLOWVALUE_V
std_inner_red = dict_battery_ref.REDVALUE_V

cur_volt = volt.pop()
cur_inner = inner.pop()

'''create btrundata'''
values = {}
btrundata_ref = api.btrundata_create(values)

'''update batterys red yellow and red values
   update batterys status'''

'''update battery current inner, vol , forcast and so on
   update battery data time
   update battery status'''