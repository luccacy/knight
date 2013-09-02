'''
Created on 2013-8-31

@author: zhouyu
'''
from knight.client import client

c = client.HTTPClient()

c.set_management_url('http://127.0.0.1:8989')

'''create task'''
'''
body = {'tasks' : {'port' : '1'}}
resp, body = c.post('/tasks', body=body)
body = {'tasks' : {'port' : '1'}}
resp, body = c.post('/tasks', body=body)
body = {'tasks' : {'port' : '2'}}
resp, body = c.post('/tasks', body=body)
print resp
print body

'''
'''list tasks'''

resp, body = c.get('/tasks')
print resp
print body

