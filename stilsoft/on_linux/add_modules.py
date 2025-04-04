import requests
import json


token = ''
url='https://gate.synerget.ru:8179'


def get_token(login='admin', password='adm777'):
    global url
    creds = {       
        'login': login,
        'password': password,
        'hash': 'edab4970-4d9b-11ef-a454-b1120eae1a88'
        }
    resp = requests.post(url+'/api/auth/login', json=creds, verify=False)
    bearer = (f'Bearer {resp.json()["access_token"]}')
        
    my_token = {
        'Authorization': bearer
    }
        
    return my_token


def refresh_token(): 
        global token
        if token == '':
            token = get_token()
        else:
            token = token


def get_node(type):
    global url
    video_list =['Сервер-видеонаблюдения','сервер-видеонаблюдения','Видео-сервер','видео-сервер']
    app_list = ['Сервер-приложений']
    if type == 'video':
        search = video_list
    elif type == 'app':
        search = app_list     
    resp = requests.get(url + '/api/data/system/node', headers = get_token(), verify = False)
    for item in resp.json()['data']:
        if item['title'] in search:
            return item['id'] 


def add_suml():
    global url
    refresh_token()    
    cams = input('Количество камер: ')
                       
    for i in range(0, int(cams)):
            
        if i <10:
            cam_pref = 1000
        else:
            cam_pref = 100     
        #body = '{'+f'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"{self.get_node('video')}","title":"new_cam_suml_{i}","zone":null,"settings":'+'{'+f'"ip":"192.168.201.126","login":"admin","password":"admin","path":"/onvif/device_service","port":1000{i},"maxArchiveSize":"1 GB","archiveLocation":"/archive","sourceTransport":"udp"'+'}'+',"subsystem":"video","type":"sdp858i"'+'}'
        body = '{'+f'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"{get_node('video')}","title":"Камера {cam_pref}{i}","zone":null,"settings":'+'{'+f'"ip":"192.168.202.200","login":"admin","password":"admin","path":"","port":{cam_pref}{i},"useMediamtx":true,"maxArchiveSize":"1 GB","archiveLocation":"/archive","sourceTransport":"udp"'+'}'+',"subsystem":"video","type":"sdp858i"'+'}'
        body_ = body = json.loads(body)
        req = requests.post(url +'/api/data/system/module', headers=token, json=body_, verify=False)
        print(f'Камера {cam_pref}{i} {i+1}/{cams}> [{req}]')    


add_suml()                       


