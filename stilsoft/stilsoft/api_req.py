from ApiRes import ApiRes
from ApiSsku import ApiSsku
import requests
import msgpack
import json
import os
import time
from time import sleep
import warnings
from threading import Timer
import ast
import datetime
import allure

base_url = 'https://gate.synerget.ru:8179'
api = ApiRes(base_url)
ssku = ApiSsku(base_url)

def repeater(interval, function):
        warnings.filterwarnings('ignore')
        Timer(interval, repeater, [interval, function]).start()
        function()

def start():
    #api.set_time()
    #ssku.glob_start_time=time.time()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('1 - Муром')
    print('2 - Гелиос')
    print('3 - ССКУ')
    spo = input('Введите номер проекта: ')
    if spo =='1':
        
        print('0 - выход')
        print('1 - вывод нотификаций для модулей')
        print('2 - вывод множества нотификаций для модулей')
        print('3 - добавление объектов на план-схему')
        print('4 - добавление отладочных целей на план-схему')
        print('5 - удаление панорамы')
        print('6 - добавление пользователя')
        print('7 - добавление множества пользователей')
        print('8 - смена камер в ячейках попеременно')
        com = input('Введите номер скрипта: ')
        if com == '1':
            api.notifications()
        elif com == '2':
            api.notif()
        elif com == '3':
            api.add_99_targets()
        elif com == '4':
            api.add_debug()
        elif com == '5':
            api.del_panorama()
        elif com == '6':
            api.add_user()
        elif com == '7':
            api.add_users()
        elif com == '8':
            api.change_ip()    
        elif com == '0':
            exit(0)
        time.sleep(4)    
        start()

    elif spo == '2':
        print('0 -выход')
        print('1 - добавление пользователя')
        print('2 - добавление множества пользователей')
        print('3 - добавление камер(модулей)')
        print('4 - вывод нотификаций для модуля')
        print('5 - вывод множества нотификаций для модулей')
       
        com_g = input('введите номер скрипта: ')
        if com_g == '0':
            exit(0)
        elif com_g == '1':
            api.add_user()
        elif com_g == '2':
            api.add_users()    
        elif com_g == '3':
            api.set_cams()
        elif com_g == '4':
            api.notifications()
        elif com_g =='5':
            api.notif()                
        start()

    elif spo == '3':
        print('1 - добавление камер')
        print('2 - добавление моковой камеры')
        print('3 - удаление модуля')
        print('4 - вывод нотификаций')
        print('5 - постман')
        print('6 - ручной инцидент с камеры')
        print('8 - вывод всех нотификаций')
        print('9 - добавление камер')
        print('10 - добавление эмуляторов камер')
        com_ssku = input('Введите номер скрипта: ')
        if  com_ssku == '1':
            ssku.set_cams()
        elif com_ssku == '2':
            ssku.set_mock_cams()
        elif com_ssku == '3':
            ssku.del_cams()    
        elif com_ssku == '4':
            ssku.notifications()
        elif com_ssku == '5':
            ssku.postman()
        elif com_ssku == '6':
            ssku.post_incident()
        elif com_ssku == '7':
            ssku.auth_cpu()
        elif com_ssku == '8':
                   
            ssku.all_notifications()    
        elif com_ssku == '9':
            ssku.add_module()
        elif com_ssku == '10':
            ssku.add_suml()

        elif com_ssku == '99':
            print(type(api.get_file_token())) 
            sleep(5)
             
        start()
  
        
#repeater(30, api.refresh_token)
#start()




def get_presets():
    warnings.filterwarnings('ignore')
    head = {
            'Authorization': api.small_token(),
            'Content-type': 'application/x-msgpack'
            }
    msp_null = msgpack.packb(None) 
    resp = requests.post('https://gate.synerget.ru:8179/api/modules/'+ api.get_881() +'/PTZGetPresets', headers = head, data=msp_null, verify = False)
    
    return (msgpack.unpackb(resp.content))


def get_servers():
    
    resp = requests.get(base_url+'/api/data/system/node',headers=ssku.get_token(), verify=False)
           
    return (resp.json())


def get_node_list():
    body_ = {"limit": 1, "offset": 1, "sort": "test_node_3", "sortAsc":True, "title": "test_node_3"}
    resp = requests.post(base_url+'/api/data/system/node/list',headers=ssku.get_token(), json=body_, verify=False)
    return(resp.json())


def mode_read():
    warnings.filterwarnings('ignore')
    body_ = '{'+'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"7c51643b-9d17-4af5-bb18-68addd812c4c","node":"0c933048-e954-48eb-b1cf-563812070c5d","title":"test_cam_1_read","zone":null,"subsystem":"video","type":"onvifcamera","settings":{"ip":"172.18.18.141","port":80,"onvif":{"login":"admin","password":"admin"},"webrtc":{"startVideoHeight":300},"rtsp":{"sourceTransport":["tcp","udp"]},"archive":{"maxArchiveSize":"1 GB","archiveLocation":"../archive","mode":"read"'+'}'+'}'+'}'
    body = json.loads(body_)
    resp = requests.put(base_url+'/api/data/system/module/7c51643b-9d17-4af5-bb18-68addd812c4c',headers=api.get_token(), json = body, verify=False)
    return(resp)


def add_user_murom(): 
    warnings.filterwarnings('ignore')
    name = input('Введите имя: ')
    login = input('Введите логин: ')
    password = input('Введите пароль: ')

    b = '{'+f'"name":"{name}","login":"{login}","password":"{password}","accessCard":"","role":"admin", "active":true, "surname":"","middleName":"", "data":'+'{'+'}'+'}'
    body = json.loads(b)
    resp = requests.post(base_url+'/api/data/security/user', headers=api.get_token(), json=body, verify=False) 
    return(resp)


def get_presets():
    os.system('cls')
    warnings.filterwarnings('ignore')
    head = {
        'Authorization': api.small_token(),
        'Content-type': 'application/x-msgpack'
                }
    body = None
    msp = msgpack.packb(body)
    resp = requests.post(base_url + f'/api/modules/{api.get_881()}/PTZ/GetPresets/', headers=head, data=msp, verify=False) 
    
    print(msgpack.unpackb(resp.content))


def get_preset_100():
    os.system('cls')
    warnings.filterwarnings('ignore')
    head = {
        'Authorization': api.small_token(),
        'Content-type': 'application/x-msgpack'
                }
    body = None
    msp = msgpack.packb(body)
    resp = requests.post(base_url + f'/api/modules/{api.get_881()}/SetTransportState/', headers=head, data=msp, verify=False) 
    
    print(msgpack.unpackb(resp.content))
        

#print(api.timer())

#print(api.refresh_token())

#get_preset_100()
#print(api.refresh_token())

def ch_loc_state():
    warnings.filterwarnings('ignore')
    head = {
        'Authorization': api.small_token(),
        'Content-type': 'application/x-msgpack'
                }
    nul=None
    msp_null = msgpack.packb(nul)
    resp = requests.post(base_url+f'/api/modules/{api.get_177()}/CurrentState',headers=head, data=msp_null, verify=False )
    
    return msgpack.unpackb(resp.content)['state']


def ch_loc():
    warnings.filterwarnings('ignore')
  
    body_1t = '{"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":'+f'"{api.get_177()}"'+',"node":'+f'"{api.get_node()}"'+',"title":"Радиолокатор","zone":null,"subsystem":"misc","type":"sts177","settings":{"ip":"192.168.202.101","port":7001'+'}'+'}'
    body_2t = '{"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":'+f'"{api.get_177()}"'+',"node":'+f'"{api.get_node()}"'+',"title":"Радиолокатор","zone":null,"subsystem":"misc","type":"sts177","settings":{"ip":"192.168.202.61","port":7001'+'}'+'}'
    body_1=json.loads(body_1t)
    body_2=json.loads(body_2t)
    for _ in range(30):
        resp=requests.put(base_url+f'/api/data/system/module/{api.get_177()}',headers=api.get_token(), json=body_1,verify=False)
        print(resp)
        if ch_loc_state()!=None:
            print("WARNING")
        sleep(1)
        resp=requests.put(base_url+f'/api/data/system/module/{api.get_177()}',headers=api.get_token(), json=body_2,verify=False)
        print(resp)
        if ch_loc_state()==None:
            print("WARNING")
        sleep(1)


def check_event():
    os.system('cls')
    warnings.filterwarnings('ignore')
    ssku.refresh_f_token()
    head=ssku.get_file_token()
    notif_body = json.loads('{"codes":"","sources":"","timeRange":null}')
    notif_count = requests.post(base_url+'/api/data/events/history/count', headers=ast.literal_eval(head), json=notif_body, verify=False ).json()['data']['count']
    body=json.loads('{"codes":"","sources":"","timeRange":null,"sort":{"sortAsc":false,"sortBy":"timestamp"},"limit":{'+f'"limit":{int(notif_count)},"offset":0'+'}'+'}')
    resp=requests.post(base_url+f'/api/data/events/history/list', headers=ast.literal_eval(head), json=body, verify=False)
    num=0
    print(notif_count)
    time_start = datetime.datetime.now()
    for _ in range(len(resp.json()['data'])):
        
        if resp.json()['data'][_]['sourceName'] == 'Камера № 7 (каб. 5)':
        #if resp.json()['data'][_]['source'] == '817c8a2b-2618-40f9-a1b0-7bd66cf7c305':
            num+=1
            print(_)
            print(resp.json()['data'][_]['user'])    
            print(resp.json()['data'][_])

    print(f'Count = {num} of {notif_count}')
    time_fin=datetime.datetime.now()
    print(time_fin-time_start)
#check_event()

def test_auth_adm():
    creds = {       
            'login': '1234567891123456789212345612345678911234567892123456',
            'password': '1234567891123456789212345612345678911234567892123456'
            }
    resp = requests.post(base_url+'/api/auth/login', json=creds, verify=False)
    print(resp)

#test_auth_adm()

def ch_881_state():
    warnings.filterwarnings('ignore')
    head = {
        'Authorization': api.small_token(),
        'Content-type': 'application/x-msgpack'
                }
    nul={}
    msp_null = msgpack.packb(nul)
    resp = requests.post(base_url+f'/api/modules/{api.get_881()}/ModuleStateRequest',headers=head, data=msp_null, verify=False )
    
    if 'offline' in msgpack.unpackb(resp.content)['states']:
        return 'OFFLINE'
    else:
        return 'ONLINE'

#print(ch_881_state())
#ch_loc()

def change_layout():
    body = {"config":{"tabsForLayout":[{"screenIndex":0,"type":"SOT"},{"screenIndex":1,"type":"INFO_MONITOR"},{"screenIndex":2,"type":"SOT"},{"screenIndex":3,"type":"ALARM_MONITOR"}],"content":[[{"id":"ac8dda1b-919e-40b9-8cf7-40e6af26e2f3","type":"video"},{"id":"ca71e327-3bd8-4b30-bd96-335fb9866a87","type":"video"},{"id":"927ae7df-0d6b-43b7-a694-26c02d362d02","type":"video"},{"id":"b8e7875e-2cd8-47f7-b6e0-34f5ac2a0241","type":"video"},{"id":"c0bf80fa-e90f-4b31-9188-56414c4cad24","type":"video"},{"id":"15c762e5-76d4-4537-8c54-5936acbdc641","type":"video"}],[],[{"id":"927ae7df-0d6b-43b7-a694-26c02d362d02","type":"video"},{"id":"15c762e5-76d4-4537-8c54-5936acbdc641","type":"video"},{"id":"40ffc7c4-72b3-4691-aae8-6bad94ef3d49","type":"empty"},{"id":"6468c15c-e837-4ef2-9809-bbf45e31ec61","type":"video"},{"id":"4d95ad3d-143e-4147-a45d-a8cc5292f3d1","type":"video"}],[]],"type":["6","auto","5","auto"]},"img":"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD","shared":False,"title":"INEP"}
    
    resp = requests.put(base_url+'/api/data/ui/layout/72e1a7bd-4b36-483a-a488-39d6424ad9c7', headers=ssku.get_token(), json=body, verify=False)


    print(resp.json())

#change_layout()

def check_link():
    os.system('cls')
    warnings.filterwarnings('ignore')
    resp = requests.get(base_url+'/api/data/system/objectlink/member/d0112e5b-e42a-4b06-a4fc-23bf4079c5fc', headers=api.get_token(),verify=False)
    print(resp.json())

def check_logout():
    os.system('cls')
    resp = requests.post(base_url+'api/auth/logout',headers=api.get_token(),verify=False)
    print(resp.status_code)

def check_sprint():
    os.system('cls')
    warnings.filterwarnings('ignore')
    resp = requests.post(base_url+'/api/modules/0f23ce0e-e6fd-434e-8446-0a7fc4da40df/MediaStream/ToggleSourceReading', headers=ssku.get_token(),verify=False)
    print(resp.json())


check_sprint()
    
    