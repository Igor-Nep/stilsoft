import requests
import allure
from ApiRes import ApiRes
import warnings
import json
from time import sleep
import msgpack
import random
import logging


base_url = 'https://gate.synerget.ru:8179'
api = ApiRes(base_url)
        
warnings.filterwarnings('ignore')

valid_8815 = '{"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":'+f'"{api.get_8815()}","node":"{api.get_node()}"'+',"title":"Камера тепловизионная","zone":null,"subsystem":"video","type":"termalcamera","settings":'+'{'+'"ip":"172.18.18.249","port":8271,"rtsp":'+'{'+'"login":"admin","password":"admin"'+'}'+',"deviceType":"svk8815m"'+'}'+'}'
invalid_8815 = '{"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":'+f'"{api.get_8815()}","node":"{api.get_node()}"'+',"title":"Камера тепловизионная","zone":null,"subsystem":"video","type":"termalcamera","settings":'+'{'+'"ip":"172.18.18.24","port":8271,"rtsp":'+'{'+'"login":"admin","password":"admin"'+'}'+',"deviceType":"svk8815m"'+'}'+'}'

valid_8083 = '{"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":'+f'"{api.get_8083()}","node":"{api.get_node()}"'+',"title":"Камера дальнего обзора","zone":null,"settings":{"ip":"172.18.18.195","port":80,"onvif":{"login":"admin","password":"admin"'+'}'+'}'+',"subsystem":"video","type":"sdp8083"}'
invalid_8083 = '{"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":'+f'"{api.get_8083()}","node":"{api.get_node()}"'+',"title":"Камера дальнего обзора","zone":null,"settings":{"ip":"172.18.18.19","port":80,"onvif":{"login":"admin","password":"admin"'+'}'+'}'+',"subsystem":"video","type":"sdp8083"}'

body_v_8083=json.loads(valid_8083)
body_inv_8083=json.loads(invalid_8083)

body_v_8815=json.loads(valid_8815)
body_inv_8815=json.loads(invalid_8815)

for _ in range(20):
    resp1=requests.put(base_url+f'/api/data/system/module/{api.get_8083()}',headers=api.get_token(), json=body_v_8083,verify=False)
    resp2=requests.put(base_url+f'/api/data/system/module/{api.get_8815()}',headers=api.get_token(), json=body_inv_8815,verify=False)
    print('Валидный 8083 невалидный 8815')
    print(resp1)
    print(resp2)
    sleep(10)
    
    resp1=requests.put(base_url+f'/api/data/system/module/{api.get_8083()}',headers=api.get_token(), json=body_inv_8083,verify=False)
    resp2=requests.put(base_url+f'/api/data/system/module/{api.get_8815()}',headers=api.get_token(), json=body_v_8815,verify=False)
    print('Валидный 8815 невалидный 8083')
    print(resp1)
    print(resp2)
    sleep(10)
    
    resp1=requests.put(base_url+f'/api/data/system/module/{api.get_8083()}',headers=api.get_token(), json=body_v_8083,verify=False)
    resp2=requests.put(base_url+f'/api/data/system/module/{api.get_8815()}',headers=api.get_token(), json=body_inv_8815,verify=False)
    print('Валидный 8083 невалидный 8815')
    print(resp1)
    print(resp2)
    sleep(5)

    resp1=requests.put(base_url+f'/api/data/system/module/{api.get_8083()}',headers=api.get_token(), json=body_inv_8083,verify=False)
    resp2=requests.put(base_url+f'/api/data/system/module/{api.get_8815()}',headers=api.get_token(), json=body_v_8815,verify=False)
    print('Валидный 8815 невалидный 8083')
    print(resp1)
    print(resp2)
    sleep(10)

    resp1=requests.put(base_url+f'/api/data/system/module/{api.get_8083()}',headers=api.get_token(), json=body_v_8083,verify=False)
    resp2=requests.put(base_url+f'/api/data/system/module/{api.get_8815()}',headers=api.get_token(), json=body_inv_8815,verify=False)
    print('Валидный 8083 невалидный 8815')
    print(resp1)
    print(resp2)
    sleep(10)

    resp1=requests.put(base_url+f'/api/data/system/module/{api.get_8083()}',headers=api.get_token(), json=body_inv_8083,verify=False)
    resp2=requests.put(base_url+f'/api/data/system/module/{api.get_8815()}',headers=api.get_token(), json=body_v_8815,verify=False)
    print('Валидный 8815 невалидный 8083')
    print(resp1)
    print(resp2)
    sleep(5)      